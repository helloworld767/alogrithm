s_min= 3
s_max= 5
a = '/'
s = 'abcd/efg/hijk'
s_min = int(s_min)
s_max = int(s_max)

s = s.split(a)
res = []
i = 0
while i < len(s):
    if i == 0:
        if len(s[i]) < s_min and s_min <= len(s[i]) + len(s[i + 1]) + 1 < s_max:
            res.append(s[i] + a+ s[i + 1])
            i += 1
        else:
            res.append(s[i])
    elif i == len(s) - 1:
        if len(s[i]) < s_min and s_min <= len(s[i]) + len(res[-1]) + 1 < s_max:
            res[-1] += a+ s[i]
        else:
            res.append(s[i])
    else:
        if len(s[i]) < s_min and s_min <= len(s[i]) + len(res[-1]) + 1 < s_max:
            res[-1] += a+ s[i]
        elif len(s[i]) < s_min and s_min <= len(s[i]) + len(s[i + 1]) + 1 < s_max:
            res.append(s[i] + a + s[i + 1])
            i += 1
        else:
            res.append(s[i])
    i += 1
print(' '.join(res))


0