A = [4, 1, 2, 3]
dp = [[0 for i in range(len(A))] for j in range(len(A))]
for i in range(len(A) - 2, -1, -1):
    for j in range(i + 1, len(A)):
        cost = sum(A[i: j + 1])
        dp[i][j] = float('inf')
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + cost)
print(dp)