# def dfs(maze, x, y, hole, dp, dir):
#     dx = [0, 0, 1, -1]
#     dy = [1, -1, 0, 0]
#     direction = ['r', 'l', 'd', 'u']
#     for i in range(4):
#         newx = x
#         newy = y
#         d = 0
#         while 0 <= newx + dx[i] < len(maze) and 0 <= newy + dy[i] < len(maze[0]) and maze[newx + dx[i]][newy + dy[i]] == 0:
#             newx += dx[i]
#             newy += dy[i]
#             d += 1
#             if [newx, newy] == hole:
#                 if dp[newx][newy] > dp[x][y] + d:
#                     res[0] = dir + direction[i]
#                     dp[newx][newy] = dp[x][y] + d
#                 elif dp[newx][newy] == dp[x][y] + d:
#                     res[0] = min(res[0], dir + direction[i])
#                 return
#
#         if dp[newx][newy] > dp[x][y] + d:
#             dp[newx][newy] = dp[x][y] + d
#             dfs(maze, newx, newy, hole, dp, dir + direction[i])
#
#
# maze = [[0,0,0],[0,0,0],[0,0,0]]
# ball = [0,0]
# hole = [1,2]
# res = ['z']
# dp = [[float('inf') for i in range(len(maze[0]))] for j in range(len(maze))]
# dp[ball[0]][ball[1]] = 0
# dfs(maze, ball[0], ball[1], hole, dp, '')
# print(res)


# def dfs(x, y, maps, dp):
#     if maps[x][y] == 'T':
#         return
#     for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#         newx = x + dx
#         newy = y + dy
#         if 0 <= newx < len(maps) and 0 <= newy < len(maps[0]) and maps[newx][newy] in '.T':
#             if dp[newx][newy] > dp[x][y] + 1:
#                 dp[newx][newy] = 1 + dp[x][y]
#                 dfs(newx, newy, maps, dp)
#
#
# maps = ["S.","#T"]
# dp = [[float('inf') for i in range(len(maps[0]))] for j in range(len(maps))]
# for i in range(len(maps)):
#     for j in range(len(maps[0])):
#         if maps[i][j] == 'S':
#             dp[i][j] = 0
#             dfs(i, j, maps, dp)
#         elif maps[i][j] == 'T':
#             end = [i, j]
# print(dp[end[0]][end[1]])

num = -1
count = 0
# while num != 0:
#     print(num)
#     count += 1
#     num = num & (num - 1)
# print(count)
while True:
    num >>= 1
    print(num)
