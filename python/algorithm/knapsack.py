def knapSack(S, s, v, n):
    dp = [0 for i in range(S+1)]
    for i in range(1, n+1):
        for w in range(S, 0, -1):
            if s[i-1]<=w:
                dp[w] = max(dp[w], dp[w-s[i-1]] + v[i-1])
    return dp[S]

v = [60, 100, 120]
s = [10, 20, 30]
S = 50
n = len(v)
# print(knapSack(S, s, v, n))

def knapsack(S, s, v, n):
    dp = [0]*(S+1)
    for i in range(1, n+1):
        for w in range(S, 0, -1):
            if s[i-1]<=w:
                dp[w] =max(dp[w], dp[w-s[i-1]] + v[i-1])
    return dp[s]