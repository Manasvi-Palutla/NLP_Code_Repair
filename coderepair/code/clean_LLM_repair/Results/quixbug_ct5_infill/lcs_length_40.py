def lcs_length(s, t):

    dp = Counter()

    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                dp.update(get_total_length(s,t))

    return max(dp.values()) if dp else 0