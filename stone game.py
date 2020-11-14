piles = [3, 9, 1, 2]
dp = [[[0 for i in range(2)] for j in range(len(piles))] for k in range(len(piles))]
for i in range(len(piles)):
    dp[i][i][0] = piles[i]

for k in range(1, len(piles)):
    for i in range(len(piles) - k):
        j = i + k
        left = piles[i] + dp[i + 1][j][1]
        right = piles[j] + dp[i][j - 1][1]
        if left > right:
            dp[i][j][0] = left
            dp[i][j][1] = dp[i + 1][j][0]
        else:
            dp[i][j][0] = right
            dp[i][j][1] = dp[i][j - 1][0]
print(dp[0][-1])