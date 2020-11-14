N = 6
dp = [[0 for i in range(2)] for i in range(N+1)]
for i in range(1, N+1):
    dp[i][0] = max(dp[i-1][0]+1, dp[i][0], dp[i-1][0] + dp[i-1][1])
    if i >= 2:
        dp[i][1] = dp[i-2][0]
print(dp)
