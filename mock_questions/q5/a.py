def countSubseq(S):
    n = len(S)
    dp = [0] * n
    total_count = 0
    
    for i in range(n):
        dp[i] = 1
        for j in range(i):
            if int(S[j]) < int(S[i]):
                dp[i] += dp[j]
        total_count += dp[i]
    
    return total_count

S = input()
print(countSubseq(S))