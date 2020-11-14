import collections
S = "zmcdqtmjl"
T = "mm"
dic = collections.defaultdict(int)
tdic = collections.Counter(T)
require = len(tdic)
form = 0
l, r = 0, 0
minlen = float('inf')
res = [-1, -1]
for r in range(len(S)):
    if S[r] in tdic:
        dic[S[r]] += 1
        if dic[S[r]] == tdic[S[r]]:
            form += 1
            if form == require:
                if r - l + 1 < minlen:
                    res = [l, r]
                    minlen = r - l + 1
        while form == require and l < r:
            if S[l] in tdic:
                dic[S[l]] -= 1
                if dic[S[l]] < tdic[S[l]]:
                    form -= 1
                elif r - l + 1 < minlen:
                    res = [l, r]
                    minlen = r - l + 1
            elif r - l < minlen:
                res = [l + 1, r]
                minlen = r - l
            l += 1
print(res)