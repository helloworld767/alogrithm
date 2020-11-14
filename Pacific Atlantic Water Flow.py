import heapq
matrix = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
m, n = len(matrix), len(matrix[0])
visited = [[False for i in range(n)] for j in range(m)]
p = [[False for i in range(n)] for j in range(m)]
a = [[False for i in range(n)] for j in range(m)]
heap, res = [], []
for i in range(m):
    for j in range(n):
        if i == 0 or j == 0:
            heapq.heappush(heap, [-matrix[i][j], i, j])
            p[i][j] = True
            visited[i][j] = True
while heap:
    height, x, y = heapq.heappop(heap)
    height = -height
    for newx, newy in ((x + 1, y), (x, y + 1)):
        if 0 <= newx < m and 0 <= newy < n and not visited[newx][newy]:
            if height <= matrix[newx][newy] and p[x][y]:
                p[newx][newy] = True
                visited[newx][newy] = True
                heapq.heappush(heap, [-matrix[newx][newy], newx, newy])
visited = [[False for i in range(n)] for j in range(m)]
heap = []
for i in range(m):
    for j in range(n):
        if i == m - 1 or j == n - 1:
            heapq.heappush(heap, [-matrix[i][j], i, j])
            a[i][j] = True
            visited[i][j] = True
while heap:
    height, x, y = heapq.heappop(heap)
    height = -height
    for newx, newy in ((x - 1, y), (x, y - 1)):
        if 0 <= newx < m and 0 <= newy < n and not visited[newx][newy]:
            if height <= matrix[newx][newy] and a[x][y]:
                a[newx][newy] = True
                visited[newx][newy] = True
                heapq.heappush(heap, [-matrix[newx][newy], newx, newy])
for i in range(m):
    for j in range(n):
        if a[i][j] and p[i][j]:
            res.append([i, j])

print(res)
print(p)
print(a)