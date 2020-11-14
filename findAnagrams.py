import collections
s = "abab"
p = "ab"
l, r = 0, 0
pdic = collections.Counter(p)
tdic = collections.defaultdict(int)
require = len(pdic)
form = 0
state = 0
res = []
for r in range(len(s)):
    if s[r] not in pdic:
        state = 0
        form = 0
        tdic.clear()
        continue

    if state == 0 and s[r] in pdic:
        l = r
        state = 1

    tdic[s[r]] += 1
    if tdic[s[r]] == pdic[s[r]]:
        form += 1
        if form == require:
            res.append(l)

    while (form == require or tdic[s[r]] > pdic[s[r]]) and l < r:
        tdic[s[l]] -= 1
        if tdic[s[l]] < pdic[s[l]]:
            form -= 1
        l += 1
print(res)
