# def search(v, w):
#     if w == 0 or not v:
#         return 1
#     if sum(v) <= w:
#         return 2 ** len(v)
#     if v[0] <= w:
#         return search(v[1:], w-v[0]) + search(v[1:], w)
#     else:
#         return search(v[1:], w)
#
#
# v = [1, 2, 4]
# w = 10
# dp = {}
# print(search(0, v, w))
# print(dp)

import collections
n, k = 6, 3
a = [1, 3, 5, 2, 5, 4]
t = [1, 1, 0, 1, 0, 0]


def help(a, t, k):
    res = 0
    for i in range(len(a)):
        if t[i] == 1:
            res += a[i]
    s, temp = 0, 0
    stack = collections.deque()
    for i in range(len(a)):
        if stack and i - stack[0] >= k:
            index = stack.popleft()
            s -= a[index]
        if t[i] == 0:
            stack.append(i)
            s += a[i]
            temp = max(temp, s)
    return res, temp



print(help(a, t, k))