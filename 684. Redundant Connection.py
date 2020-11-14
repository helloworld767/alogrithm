import collections
edges = [[9,10],[5,8],[2,6],[1,5],[3,8],[4,9],[8,10],[4,10],[6,8],[7,9]]
graph = collections.defaultdict(list)
for begin, end in edges:
    graph[begin].append(end)
    graph[end].append(begin)
q = []
visited = []
degree = {}
for i in graph:
    degree[i] = len(graph[i])
    if len(graph[i]) == 1:
        q.append(i)
        visited.append(i)

while q:
    node = q.pop(0)
    for i in graph[node]:
        if i not in visited:
            degree[i] -= 1
            if degree[i] == 1:
                q.append(i)
                visited.append(i)

for i in range(len(edges) - 1, -1, -1):
    if edges[i][0] not in visited and edges[i][1] not in visited:
        print(edges[i])
        break
