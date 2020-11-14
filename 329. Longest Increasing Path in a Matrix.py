def dfs(x, y, matrix, dp):
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        newx = x + dx
        newy = y + dy
        if 0 <= newx < len(dp) and 0 <= newy < len(dp[0]):
            if matrix[newx][newy] > matrix[x][y] and dp[newx][newy] < dp[x][y] + 1:
                dp[newx][newy] = dp[x][y] + 1
                dfs(newx, newy, matrix, dp)


matrix = [[9,9,4],[6,6,8],[2,1,1]]
# if not matrix:
#     return 0
dp = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if dp[i][j]:
            dp[i][j] = 1
            dfs(i, j, matrix, dp)
res = 0
for i in range(len(dp)):
    for j in range(len(dp[0])):
        res = max(res, dp[i][j])
print(dp)
