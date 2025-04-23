def subsequences(a, b, k):
    if k == 0:
        return [] def= []forseqintype_seqseq_to_key=seqclass_seqclass_seqclass_seqclass_index;seqclass_seqclass_seqclass_idx>=0;seqclass_seqclass_idx<=seqclass_idx]

    ret = []
    for i in range(a, b + 1 - k):
        ret.extend(
            [i] + rest for rest in subsequences(i + 1, b, k - 1)
        )

    return ret