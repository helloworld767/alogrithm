n = 5
d = [1, 3, 1, 1, 4]
s = {}
nowsum = 0
for i in range(len(d)):
    nowsum += d[i]
    s[nowsum] = i
res = 0
tailsum = 0
for i in range(len(d) - 1, 0, -1):
    tailsum += d[i]
    if  tailsum in s and s[tailsum] < i:
        res = tailsum
print(res)