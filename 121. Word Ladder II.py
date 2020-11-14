import collections
start = "hit"
end = "cog"
dict = {"hot","dot","dog","lot","log"}
graph = collections.defaultdict(list)
dict.add(start)
dict.add(end)
for word in dict:
    for i in range(len(word)):
        t = word[:i] + '*' + word[i + 1:]
        graph[t].append(word)
visited = {word: [] for word in dict}
visited[start] = [1]
min_dist = {word: float('inf') for word in dict}
min_dist[start] = 1
q = collections.deque([[start, 1]])
res = []
while q:
    word, dist = q.popleft()
    for i in range(len(word)):
        t = word[:i] + '*' + word[i + 1:]
        for nextword in graph[t]:
            if not visited[nextword] or min_dist[nextword] >= dist + 1:
                min_dist[nextword] = dist + 1
                q.append([nextword, dist + 1])
                visited[nextword].append(word)


def dfs(visited, word, start):
    if visited[word] == [start]:
        return [[start, word]]
    res = []
    for lastword in visited[word]:
        for s in dfs(visited, lastword, start):
            res.append(s + [word])
    return res


print(visited)
print(dfs(visited, end, start))