# m = ['..X.X', 'XX...']
# dp = [[0 for i in range(len(m[0]))] for j in range(2)]
# for i in range(2):
#     for j in range(len(m[0])):
#         if m[i][j] == 'X':
#             continue
#         if j - 1 >= 0:
#             dp[i][j] = dp[i][j-1] + 1
#         if i == 0 and j - 1 >= 0:
#             dp[i][j] = dp[i+1][j-1] + 1
#         if i == 1 and j - 1 >= 0:
#             dp[i][j] = dp[i-1][j-1] + 1
# print(dp[-1][-1])


# n, k, l, r = 9, 1, 1, 3
# l = list(range(l, r+1))
# res = [0]
# def search(n, j, l, subset):
#     if n == 0:
#         if sum(subset) % k == 0:
#             res[0] += 1
#         return
#     for i in range(j, len(l)):
#         search(n-1, 0, l, subset+[l[i]])
# search(n, 0, l, [])
# print(res[0] % (1e9+7))

# rotateArray = [6501,6828,6963,7036,7422,7674,8146,8468,8704,8717,9170,9359,9719,9895,9896,9913,9962,154,293,334,492,1323,1479,1539,1727,1870,1943,2383,2392,2996,3282,3812,3903,4465,4605,4665,4772,4828,5142,5437,5448,5668,5706,5725,6300,6335]
# l, r = 0, len(rotateArray) - 1
# while l < r:
#     mid = (l + r) // 2
#     if rotateArray[l] <= rotateArray[r]:
#         print(rotateArray[l])
#     if rotateArray[mid] >= rotateArray[l]:
#         l = mid + 1
#     else:
#         r = mid
# print(rotateArray[l])

# n = 3
# num = 0
# while n != 0:
#     num += 1
#     n = n & (n - 1)
# print(num)
# s = "3[a2[c]]"
# num = 0
# nums = []
# strings = []
# string = ''
# flag = 0
# for i in s:
#     if i.isdigit():
#         num = num * 10 + int(i)
#         if string != '':
#             strings.append(string)
#             string = ''
#             flag = 1
#     elif i == '[':
#         nums.append(num)
#         num = 0
#     elif i == ']':
#         if string != '':
#             strings.append(string)
#         tn = nums.pop()
#         ts = strings.pop()
#         if flag:
#             strings[-1] += ts * tn
#             flag = 0
#         else:
#             strings.append(ts * tn)
#         string = ''
#     else:
#         string += i
# # while nums:
# #     string = strings.pop()
# #     num = nums.pop()
# #     strings.append(string * num)
# print(''.join(strings))

# a, b = 1, 2
# t = a
# a = 0
# print(t)

# a = 10
# print(a & -a)

class spam:
    num = 0
    @staticmethod
    def count():
        spam.num += 1
        return
    def __init__(self):
        self.count()
        return

class other(spam):
    num = 0

class sup(spam):
    num = 0

a = spam()
b = spam()
c = spam()
a1 = other()
b1 = other()
# c1 = other()
print(a.num, b.num, c.num, a1.num, b1.num)
print(spam.num)

# def get():
#     return [lambda x: i * x for i in range(4)]
#
#
# print(list(m(8) for m in get()))

