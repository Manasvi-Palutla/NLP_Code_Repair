import argparse
import copy
import json
import sys
import types
import shutil
import signal
import os
from io import StringIO

sys.dont_write_bytecode = True

graph_based = ["breadth_first_search", "depth_first_search", "detect_cycle",
               "minimum_spanning_tree", "reverse_linked_list",
               "shortest_path_length", "shortest_path_lengths",
               "shortest_paths", "topological_ordering"]

# Base directory paths for Colab
BASE_DIR = "/content/coderepair/code/clean_LLM_repair/QuixBugs"
CORRECT_PROG_DIR = os.path.join(BASE_DIR, "correct_python_programs")
JSON_TESTCASE_DIR = os.path.join(BASE_DIR, "json_testcases")
PF_JSON_PATH = os.path.join(BASE_DIR, "Python", "pf.json")

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        sys.stdout = self._stdout
        del self._stringio

def handler(signum, frame):
    raise Exception("Timeout")

def py_try(algo, *args):
    try:
        if f"correct_python_programs.{algo}" in sys.modules:
            del sys.modules[f"correct_python_programs.{algo}"]
        signal.signal(signal.SIGALRM, handler)
        signal.alarm(5)
        module = __import__(f"correct_python_programs.{algo}")
        fx = getattr(module, algo)
        re = getattr(fx, algo)(*args)
        re = prettyprint(re)
        signal.alarm(0)
        return re
    except:
        return sys.exc_info()

def py_try_test(algo):
    try:
        if f"correct_python_programs.{algo}_test" in sys.modules:
            del sys.modules[f"correct_python_programs.{algo}_test"]
            del sys.modules[f"correct_python_programs.{algo}"]
        signal.signal(signal.SIGALRM, handler)
        signal.alarm(5)
        correct_module = __import__(f"correct_python_programs.{algo}_test")
        correct_fx = getattr(correct_module, f"{algo}_test")
        with Capturing() as output:
            getattr(correct_fx, "main")()
        signal.alarm(0)
        return ["\n".join(output)]
    except:
        return sys.exc_info()

def prettyprint(o):
    return f"(generator) {list(o)}" if isinstance(o, types.GeneratorType) else str(o)

def move_file_and_copy(src, dest, prefix, postfix):
    with open(src, 'r') as f:
        s = f.read()
    shutil.copy(dest, dest + ".bak")
    with open(dest, 'w') as f:
        f.write(prefix + s + postfix if prefix and postfix else s)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--bug', type=str, help='bug to evaluate')
    parser.add_argument('--file', type=str, help='proposed fix in a file')
    parser.add_argument('--add_pf', action='store_true', default=False)
    args = parser.parse_args()

    correct, patch = [], []
    prefix, postfix = None, None

    if args.add_pf:
        with open(PF_JSON_PATH, 'r') as f:
            data = json.load(f)
            if args.bug in data:
                prefix = data[args.bug]["prefix"]
                postfix = data[args.bug]["postfix"]

    dest_path = os.path.join(CORRECT_PROG_DIR, f"{args.bug}.py")

    if args.bug in graph_based:
        correct = py_try_test(args.bug)
        move_file_and_copy(args.file, dest_path, prefix, postfix)
        patch = py_try_test(args.bug)
        shutil.move(dest_path + ".bak", dest_path)
    else:
        with open(os.path.join(JSON_TESTCASE_DIR, f"{args.bug}.json"), 'r') as f:
            for line in f:
                py_testcase = json.loads(line)
                test_in, test_out = py_testcase
                if not isinstance(test_in, list):
                    test_in = [test_in]
                c = py_try(args.bug, *copy.deepcopy(test_in))
                correct.append(c)
                move_file_and_copy(args.file, dest_path, prefix, postfix)
                o = py_try(args.bug, *copy.deepcopy(test_in))
                patch.append(o)
                shutil.move(dest_path + ".bak", dest_path)
                if c != o:
                    print("This is not a correct patch")
                    sys.exit(1)

    if patch != correct:
        print("This is not a correct patch")
        sys.exit(1)

    print("This is a plausible patch")
    sys.exit(0)

if __name__ == "__main__":
    main()
