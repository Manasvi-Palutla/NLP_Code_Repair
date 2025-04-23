def lcs_length(s, t):

    dp = Counter()

    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                dp.add(seqno)

    return max(dp.values()) if dp else 0