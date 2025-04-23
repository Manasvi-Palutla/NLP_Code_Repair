import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, StoppingCriteria, StoppingCriteriaList
from transformers import T5ForConditionalGeneration

global_infill_stops = ['# Provide a fix for the buggy function', '// Provide a fix for the buggy function']

class SpanLM(object):
    def __init__(self, pretrained: str = "", weight=None, batch_size=1):
        print("Initializing a SpanLM based model: {} ...".format(pretrained))
        self.pretrained = pretrained
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.extra_end = None  # some models requires some ending tokens
        if 'Salesforce' in pretrained:
            self.model = T5ForConditionalGeneration.from_pretrained(pretrained)
            self.max_length = self.model.config.to_dict()['n_positions']
            self.infill_ph = "<extra_id_0>"
            self.END_ID = 2
            self.infill_ID = 32099
        elif 'facebook' in pretrained:
            if weight == 'float16':
                self.model = AutoModelForCausalLM.from_pretrained(pretrained, revision="float16", torch_dtype=torch.float16)
                self.model = self.model.half()
            else:
                self.model = AutoModelForCausalLM.from_pretrained(pretrained)
            self.max_length = self.model.config.to_dict()['max_position_embeddings']
            self.infill_ph = "<|mask:0|>"
            self.extra_end = "<|mask:1|><|mask:0|>"
            # signals the end of a generated infill
            self.EOM = "<|endofmask|>"
            self.EOM_ID = 50517
            self.BOS = "<|endoftext|>"
            self.META_FILE = "<|/ file"
        else:
            raise NotImplementedError
        print("Max length: {}".format(self.max_length))
        self.model = self.model.to(self.device)
        self.tokenizer = AutoTokenizer.from_pretrained(pretrained)
        self.batch_size = batch_size

    def build_input(self, prefix: str, suffix: str):
        if self.extra_end:
            return prefix + self.infill_ph + suffix + self.extra_end
        return prefix + self.infill_ph + suffix

    def check_input(self, prefix: str, suffix: str, buggy: str = "", use_max_length: bool = False):
        if not use_max_length:
            input_tokens = self.tokenizer.encode(self.build_input(prefix, suffix), return_tensors='pt')
            if len(input_tokens[0]) + 50 > self.max_length:
                return False
        else:
            # Check if prompt + fix_function=approx(buggy_func) will be longer than the max length
            input_tokens = self.tokenizer.encode(prefix + buggy + suffix, return_tensors='pt')
            if len(input_tokens[0]) + 110 > self.max_length:
                return False
        return True

    def model_predict(self, prefix: str, suffix: str, do_sample=False, use_max_length=False, buggy: str = "", num_samples=1000):
        if not self.check_input(prefix, suffix, buggy, use_max_length):
            return False, False, None, None
        input_tokens = self.tokenizer.encode(self.build_input(prefix, suffix), return_tensors='pt')\
            .repeat(min(num_samples, self.batch_size), 1)
        input_tokens = input_tokens.to(self.device)
        with torch.no_grad():
            if use_max_length:
                raw_o = self.model.generate(input_tokens,
                                            max_length=len(input_tokens[0])
                                                       + len(self.tokenizer.encode(buggy, return_tensors='pt')[0])
                                                       + 100,
                                            do_sample=do_sample,
                                            output_scores=True,
                                            return_dict_in_generate=True,
                                            temperature=0.8,
                                            top_p=0.95)
            else:
                raw_o = self.model.generate(input_tokens,
                                            max_length=len(input_tokens[0]) + 50,
                                            do_sample=do_sample,
                                            output_scores=True,
                                            return_dict_in_generate=True,
                                            temperature=0.8,
                                            top_p=0.95)


            entropies = []
            if 'Salesforce' in self.pretrained:
                outputs = self.tokenizer.batch_decode(raw_o.sequences, skip_special_tokens=True)
                neg_logs = -torch.log(torch.stack(raw_o.scores, dim=1).softmax(-1))
                neg_logs = torch.gather(neg_logs, 2, raw_o.sequences[:, 1:, None]).squeeze(-1)
                t_outputs = []
                for index, output in enumerate(outputs):
                    if self.END_ID in raw_o.sequences[index, 1:]:
                        min_index = (raw_o.sequences[index, 1:] == self.END_ID).nonzero(as_tuple=True)[0][0].cpu().item()
                        infill_index = (raw_o.sequences[index, 1:] == self.infill_ID).nonzero(as_tuple=True)[0][0].cpu().item()
                        entropies.append(
                            (neg_logs[index, infill_index+1:min_index].sum(-1).cpu().item() / len(neg_logs[index, infill_index+1:min_index]),
                             neg_logs[index, infill_index+1:min_index].sum(-1).cpu().item()))
                        t_outputs.append(output)
                outputs = t_outputs
            elif 'facebook' in self.pretrained:
                gen_sequences = raw_o.sequences[:, len(input_tokens[0]):]
                neg_logs = -torch.log(torch.stack(raw_o.scores, dim=1).softmax(-1))
                neg_logs = torch.gather(neg_logs, 2, gen_sequences[:, :, None]).squeeze(-1)
                outputs = self.tokenizer.batch_decode(gen_sequences, clean_up_tokenization_spaces=False)
                t_outputs = []
                for index, output in enumerate(outputs):
                    if output.startswith(self.BOS):
                        print(output)
                        assert False
                    # This is a hack to stop the prefix and suffix generated by the model to be wrong
                    # TODO: contact the developer to double check this
                    # output = output[len(self.build_input(prefix, suffix)):]
                    if self.EOM not in output:
                        print("EOM not in")
                        continue
                        # only for infilling entire function, sometimes it does not stop in time
                        # for eof_string in global_infill_stops:
                        #     if eof_string in output:
                        #         output = output[:output.index(eof_string)]
                                # return True, True, output.strip()
                        # return False, True, ""
                    output = output[:output.index(self.EOM)]
                    if self.META_FILE in output:  # removes META file token that is sometimes generated
                        output = output[:output.index(self.META_FILE)]
                    min_index = (gen_sequences[index] == self.EOM_ID).nonzero(as_tuple=True)[0][0].cpu().item()
                    entropies.append(
                        (neg_logs[index, :min_index].sum(-1).cpu().item() / (min_index + 1),
                         neg_logs[index, :min_index].sum(-1).cpu().item()))
                    t_outputs.append(output)
                outputs = t_outputs

        return True, True, outputs, entropies
