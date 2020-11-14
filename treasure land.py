map = [['O', 'O', 'O', 'O'],
     ['D', 'O', 'D', 'O'],
     ['O', 'O', 'O', 'O'],
     ['X', 'D', 'D', 'O']]


def search(x, y, mask, map, dp):
    if map[x][y] == 'X':
        return 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        newx = x + dx[i]
        newy = y + dy[i]
        if len(map) > newx >= 0 and len(map[0]) > newy >= 0 and map[newx][newy] != 'D' and mask[newx][newy] != 1:
            if mask[newx][newy] == 0:
                mask[newx][newy] = 1
                dp[x][y] = min(dp[x][y], search(newx, newy, mask, map, dp))
                if dp[newx][newy] == float('inf'):
                    mask[newx][newy] = 0
            else:
                dp[x][y] = min(dp[x][y], dp[newx][newy])
    mask[x][y] = 2
    dp[x][y] += 1
    return dp[x][y]


mask = [[0 for i in range(len(map[0]))] for j in range(len(map))]
mask[0][0] = 1
dp = [[float('inf') for i in range(len(map[0]))] for j in range(len(map))]
print(search(0, 0, mask, map, dp))
print(dp)
print(mask)

