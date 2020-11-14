import heapq
matrix = [[1,5,7],[3,7,8],[4,8,9]]
k = 4

q = [(matrix[0][0], 0, 0)]
visited = {(0, 0)}
for i in range(k):
    num, x, y = heapq.heappop(q)
    if x + 1 < len(matrix) and (x + 1, y) not in visited:
        heapq.heappush(q, (matrix[x + 1][y], x + 1, y))
        visited.add((x + 1, y))
    if y + 1 < len(matrix[0]) and (x, y + 1) not in visited:
        heapq.heappush(q, (matrix[x][y + 1], x, y + 1))
        visited.add((x, y + 1))
res, x, y = heapq.heappop(q)