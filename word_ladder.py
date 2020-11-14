import collections
start = "hit"
end = "cog"
dict = {"hot","dot","dog","lot","log"}
dict.add(start)
dict.add(end)
graph = collections.defaultdict(list)
for word in dict:
    for i in range(len(word)):
        graph[word[:i] + '*' + word[i + 1:]].append(word)

q = collections.deque()
q.append([start, 1])
visited = {start}
record = collections.defaultdict(set)
min_dist = {}
min_dist[start] = 1
flag = True

while q:
    word, dist = q.popleft()
    if not flag:
        for i in range(len(word)):
            for nextword in graph[word[:i] + '*' + word[i + 1:]]:
                if nextword == end and word != end:
                    record[nextword].add(word)

        continue
    for i in range(len(word)):
        for nextword in graph[word[:i] + '*' + word[i + 1:]]:
            if nextword not in visited:
                if nextword == end:
                    flag = False
                q.append([nextword, dist + 1])
                visited.add(nextword)
                min_dist[nextword] = dist + 1
                record[nextword].add(word)
            elif min_dist[nextword] == dist + 1:
                record[nextword].add(word)


def dfs(record, start, end):
    if start == end:
        return [[end]]
    res = []
    for word in record[end]:
        for seq in dfs(record, start, word):
            res.append(seq + [end])
    return res
print(dfs(record, start, end))
