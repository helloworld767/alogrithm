import collections
start = "a"
end = "c"
dict = ["a","b","c"]
graph = collections.defaultdict(list)
for i in range(len(dict)):
    word = list(dict[i])
    for j in range(len(word)):
        t = word[:j] + ['*'] + word[j + 1:]
        graph[tuple(t)].append(dict[i])
dist = 1
visited = {start}
q = collections.deque([[start, dist]])
while q:
    word, dist = q.popleft()
    for i in range(len(word)):
        t = tuple(word[:i] + ['*'] + word[i + 1:])
        for nextword in graph[t]:
            if nextword not in visited:
                if nextword == end:
                    print(dist + 1)
                q.append([nextword, dist + 1])
                visited.add(nextword)