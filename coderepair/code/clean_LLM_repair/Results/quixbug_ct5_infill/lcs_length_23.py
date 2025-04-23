def lcs_length(s, t):

    dp = Counter()

    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                dp[j] += 1

    return max(dp.values()) if dp else 0