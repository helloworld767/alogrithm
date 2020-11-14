dp = {}
d = 1
f = 6
target = 3

def search(d, f, target):
    if d == 0:
        if target == 0:
            return 1
        return 0
    if (target, d) in dp:
        return dp[(target, d)]
    res = 0
    for i in range(1, f + 1):
        if target - i >= 0:
            res += search(d-1, f, target - i)
    dp[(target, d)] = res
    return res


print(search(d, f, target))