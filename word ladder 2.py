import collections
beginWord = "hot"
endWord = "dog"
wordList = ["hot","dog"]

graph = collections.defaultdict(set)
if beginWord not in wordList:
    wordList.append(beginWord)
if endWord not in wordList:
    print([])

for word in wordList:
    for i in range(len(word)):
        graph[word[: i] + '*' + word[i + 1:]].add(word)

q = collections.deque()
q.append(endWord)
distance = {endWord: 0}
while q:
    word = q.popleft()
    for i in range(len(word)):
        for nextword in graph[word[: i] + '*' + word[i + 1:]]:
            if nextword not in distance:
                distance[nextword] = distance[word] + 1
                q.append(nextword)

if beginWord not in distance:
    print([])

def dfs(word, endWord, distance, path, res):
    if word == endWord:
        res.append(path)
        return

    for i in range(len(word)):
        for nextword in graph[word[: i] + '*' + word[i + 1:]]:
            if distance[nextword] == distance[word] - 1:
                dfs(nextword, endWord, distance, path + [nextword], res)
    return


res = []
dfs(beginWord, endWord, distance, [beginWord], res)
print(res)
