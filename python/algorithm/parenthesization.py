import sys
dp = [[-1 for i in range(100)] for j in range(100)]

def memo(p, i, j):
    if(i == j): return 0
    
    if(dp[i][j] != -1): return dp[i][j]
    
    dp[i][j] = sys.maxsize
    
    for k in range(i, j):
        dp[i][j] = min(dp[i][j], memo(p, i, k) + memo(p, k+1, j) + p[i-1]*p[k]*p[j])
    return dp[i][j]

def order(p, n):
    i = 1
    j = n-1
    return memo(p, i, j)

arr = [1,2,3,4]
n = len(arr)
print(order(arr, n))
    