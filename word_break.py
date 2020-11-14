s = "aaaaaaa"
wordDict = ["aaaa","aa","a"]
dp = [False for i in range(len(s)+1)]
dp[0] = -1
for i in range(1, len(s)+1):
    for j in wordDict:
        if i >= len(j):
            if dp[i-len(j)] and s[i-len(j):i] == j:
                if not dp[i]:
                    dp[i] = [i -len(j)]
                else:
                    dp[i].append(i -len(j))
# if not dp[-1]: return []
l = []
q = [dp[-1]]
res = []
index = []
while q:
    t = q.pop(0)
    for i in t:
        if dp[i] != [0] and dp[i] != -1:
            for j in dp[i]:
                if j not in index:
                    index.append(j)
            q.append(dp[i])
index.sort()
for j in index:
    if dp[j] != [0] and dp[j] != -1:
        l.append(dp[j])
l.append(dp[-1])
print(l)
def generate(l, subset, s):
    if not l:
        if s:
            subset = [s] + subset
        res.append(subset)
        return
    k = l.pop()
    for i in k:
        generate(l, [s[i:]]+subset, s[:i])
generate(l, [], s)
# res = list(map(lambda x: x[:-1], res))
print(res)