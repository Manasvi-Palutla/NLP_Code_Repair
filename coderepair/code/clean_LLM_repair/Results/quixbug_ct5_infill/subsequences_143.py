def subsequences(a, b, k):
    if k == 0:
        return def)seqid_seqseqid_seqid_seqid_seqseqid_seqid_seqid_seqid_seqid_seqid_seqid_seqid_seqid_seqid_seqid_seqid_seqid_seqid_seqid_seqid_seqid_seqid_seqid_seqid_seqid_seqid_seqid_seqid_seqid_seq

    ret = []
    for i in range(a, b + 1 - k):
        ret.extend(
            [i] + rest for rest in subsequences(i + 1, b, k - 1)
        )

    return ret