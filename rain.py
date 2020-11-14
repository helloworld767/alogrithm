import heapq
heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
heap, res = [], 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
# if not heightMap or heightMap[0]:
#     return 0
visited = [[False for i in range(len(heightMap[0]))] for j in range(len(heightMap))]

for i in range(len(heightMap)):
    for j in range(len(heightMap[0])):
        if i == 0 or j == 0 or i == len(heightMap) - 1 or j == len(heightMap[0]) - 1:
            heapq.heappush(heap, [heightMap[i][j], i, j])
            visited[i][j] = True
print(visited)
while heap:
    height, x, y = heapq.heappop(heap)
    for i in range(4):
        newx = x + dx[i]
        newy = y + dy[i]
        if 0 <= newx < len(heightMap) and 0 <= newy < len(heightMap[0]):
            if not visited[newx][newy]:
                if height > heightMap[newx][newy]:
                    res += height - heightMap[newx][newy]
                    heightMap[newx][newy] = height
                visited[newx][newy] = True
                heapq.heappush(heap, [heightMap[newx][newy], newx, newy])
print(res)