# k = 2
# prices = [2,1,4]
#
# dp = [[[0 for i in range(len(prices) + 1)] for j in range(k + 1)] for m in range(2)]
# for j in range(k+1):
#     dp[1][j][0] = -float('inf')
#
# for j in range(1, k + 1):
#     for i in range(1, len(prices) + 1):
#         dp[0][j][i] = max(dp[0][j][i - 1], dp[1][j][i - 1] + prices[i - 1])
#         dp[1][j][i] = max(dp[1][j][i - 1], dp[0][j - 1][i - 1] - prices[i - 1])
# print(dp[0][-1][-1])


# string = '12ere2'
# a = list(set(string))
# a.sort(key=string.index)
# print(''.join(a))


# candy = 4
# child = 3
# res = []
# def help(i, nums, subset):
#     if len(subset) == child - 1:
#         res.append(subset)
#         return
#     if i == len(nums):
#         return
#     for j in range(i, len(nums)):
#         help(j, nums, subset+[nums[j]])
# nums = list(range(candy+1))
# help(0, nums, [])
# print(res)
# print(len(res))
#
# for i in range(len(res)-1, -1, -1):
#     l = ['*' for k in range(candy)]
#     k = res[i][::-1]
#     a = list(set(res[i]))
#     a.sort(key=k.index)
#     for j in a:
#         # if j < len(res[i]) and res[i][j] != res[i][j-1]:
#         l.insert(j, '|')
#     print(''.join(l))


# a = [2, 3, 5, 7]
# v = [1, 5, 2, 4]
# m = 10
# dp = [[0 for i in range(m+1)] for j in range(len(a)+1)]
# for i in range(1, len(a)+1):
#     for j in range(1, m+1):
#         k = 1
#         while j >= a[i-1] * k:
#             dp[i][j] = max(dp[i-1][j], dp[i-1][j-a[i-1]*k] + v[i-1] * k)
#             k += 1
#         if j < a[i-1]:
#             dp[i][j] = dp[i-1][j]
# print(dp[-1][-1])
# print(dp)
# dp = [0 for i in range(m+1)]
# for i in range(len(a)):
#     for j in range(a[i], m+1):
#         dp[j] = max(dp[j-a[i]]+v[i], dp[j])
#     print(dp)
# print(dp[-1])


# n = 12
# prices = [2, 4]
# weights = [100, 100]
# amounts = [4, 2]
# dp = [0 for i in range(n+1)]
# for i in range(len(prices)):
#     for j in range(amounts[i]):
#         for k in range(n, prices[i]-1, -1):
#             dp[k] = max(dp[k], dp[k-prices[i]]+weights[i])
# print(dp[-1])


# n = 10
# values = [1, 2, 4]
# amounts = [2, 1, 1]
# dp = [False for i in range(n+1)]
# dp[0] = True
# for i in range(len(values)):
#     for j in range(amounts[i]):
#         for k in range(n, values[i]-1, -1):
#             dp[k] = dp[k-values[i]]
# print(sum(dp)-1)
# print(dp)

# nums = [7,2,5,10,8]
#
# n = sum(nums) // 2
# dp = [0 for i in range(n+1)]
# for i in range(len(nums)):
#     for j in range(n, nums[i]-1, -1):
#         dp[j] = max(dp[j], dp[j-nums[i]]+nums[i])
#     # print(dp[-1])
# print(dp)
# height = [[1, 3, 1, 2, 1],
# [2, 1, 3, 1, 1],
# [1, 4, 2, 6, 1],
# [1, 3, 1, 3, 1],
# [1, 1, 5, 1, 1]]
#
# if not height:
#     print(0)
#
# m = len(height)
# n = len(height[0])
# peakmap = [[float('inf')]*n for i in range(m)]
# stack = []
#
#
# for i in range(m):
#     for j in range(n):
#         if i in (0, m-1) or j in (0, n-1):
#             peakmap[i][j] = height[i][j]
#             stack.append((i, j))
#
# while stack:
#     i, j = stack.pop(0)
#     dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#     for dx, dy in dirs:
#         nx, ny = i + dx, j + dy
#         if nx < 0 or nx > m-1 or ny < 0 or ny > n-1:
#             continue
#         limit = max(peakmap[i][j], height[nx][ny])
#         if peakmap[nx][ny] > limit:
#             peakmap[nx][ny] = limit
#             stack.append((nx, ny))
# print(sum(peakmap[i][j] - height[i][j] for i in range(m) for j in range(n)))

# l = [1, 2, 5]
# res = []
# for i in l:
#     num = 0
#     while i > 0:
#         if (i+1) % 2 == 0:
#             i = i - (i+1)// 2
#         else:
#             i = i - (i+1) // 2
#         num += 1
#     res.append(num)
# for i in res:
#     print(i)
# import collections
# l = [3, 2, 4, 1, 4]
# dic = collections.Counter(l)
# res = 0
#
# while any(dic.values()):
#     for i in dic:
#         if dic[i] > 0:
#             dic[i] -= 1
#
#     res += 1
# print(res)

# l = [6, 2]
# w = [-3, 1, -2, 3, 4, 0]
# r = [[1, 2],
# [1, 3],
# [2, 4],
# [3, 5],
# [3, 6]]
# k = []
# dic = {}
# for i in r:
#     dic[i[1]] = i[0]
#     k.append(i[0])
#
# for i in range(1, l[0]):
#     if i not in k:
#         begin = i
#         break

# number = 5
# dp = [0 for i in range(number + 1)]
# dp[0] = 1
# dp[1] = 1
# for i in range(2, number + 1):
#     for j in range(1, i + 1):
#         dp[i] += dp[i - j]
# print(dp[-1])
#
# tsum = 3
# factors = []
# for i in range(1, tsum + 1):
#     if i % 2 == 1 and tsum % i == 0:
#         factors.append(i)
#     elif i % 2 == 0 and tsum % i == i // 2:
#         factors.append(i)
# res = []
# factors = factors[::-1]
# for factor in factors:
#     if factor == 1:
#         continue
#     num = tsum // factor
#     if num - factor // 2 > 0 and tsum % factor == 0:
#         nums = list(range(num - factor // 2, num + factor // 2 + 1))
#         res.append(nums)
#     elif num - factor // 2 >= 0 and tsum % factor == factor // 2:
#         nums = list(range(num - factor // 2 + 1, num + factor // 2 + 1))
#         res.append(nums)
# print(factors, res)


# import heapq
#
#
# class Solution:
#     def __init__(self):
#         self.small = []
#         self.large = []
#
#     def Insert(self, num):
#         # write code here
#         if len(self.small) == len(self.large):
#             heapq.heappush(self.large, num)
#         elif len(self.small) > len(self.large):
#             if num >= -self.small[0]:
#                 heapq.heappush(self.large, num)
#             else:
#                 heapq.heappush(self.large, -heapq.heappop(self.small))
#                 heapq.heappush(self.small, -num)
#         else:
#             if num <= self.large[0]:
#                 heapq.heappush(self.small, -num)
#             else:
#                 heapq.heappush(self.small, -heapq.heappop(self.large))
#                 heapq.heappush(self.large, num)
#
#     def GetMedian(self):
#         # write code here
#         if (len(self.small) + len(self.large)) % 2 == 0:
#             return (-self.small[0] + self.large[0]) / 2
#         else:
#             return self.large[0] if len(self.large) > len(self.small) else -self.small[0]


# import collections
# num, size = [2,3,4,2,6,2,5,1],3
# temp, res, dic = collections.deque(), [], {}
# for i in range(len(num)):
#     while temp and num[temp[-1]] < num[i]:
#         temp.pop()
#     temp.append(i)
#     if temp and temp[0] + size == i:
#         temp.popleft()
#     if i >= size - 1:
#         res.append(num[temp[0]])
# print(res)


# def dfs(m, x, y, path, visited):
#     if not path:
#         return True
#     for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
#         newx = x + dx
#         newy = y + dy
#         if 0 <= newx < len(m) and 0 <= newy < len(m[0]):
#             if m[newx][newy] == path[0] and (newx, newy) not in visited:
#                 visited.add((newx, newy))
#                 if dfs(m, newx, newy, path[1:], visited):
#                     return True
#                 visited.remove((newx, newy))
#     return False
#
#
# matrix, rows, cols, path = "ABCESFCSADEE",3,4,"ABCCED"
# m = [[0 for i in range(cols)] for j in range(rows)]
# k = 0
# for i in range(rows):
#     for j in range(cols):
#         m[i][j] = matrix[k]
#         k += 1
#
# visited = set()
# for i in range(rows):
#     for j in range(cols):
#         if m[i][j] == path[0]:
#             visited.add((i, j))
#             if dfs(m, i, j, path[1:], visited):
#                 print(True)
#             visited.remove((i, j))
# print(False)

# def dfs(x, y, rows, cols, threshold, visited):
#     res = 0
#     for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
#         newx = x + dx
#         newy = y + dy
#         if 0 <= newx < rows and 0 <= newy < cols:
#             if (newx, newy) not in visited and sum(map(int, list(str(newx) + str(newy)))) <= threshold:
#                 visited.add((newx, newy))
#                 res += dfs(newx, newy, rows, cols, threshold, visited)
#     return res + 1
#
# threshold, rows, cols  = 5,10,10
# visited = set()
# visited.add((0, 0))
# dfs(0, 0, rows, cols, threshold, visited)
# print(len(visited))

# numbers = [2,1,3,1,4]
# for i in range(len(numbers)):
#     while numbers[i] != i:
#         if numbers[i] != numbers[numbers[i]]:
#             temp = numbers[numbers[i]]
#             numbers[numbers[i]] = numbers[i]
#             numbers[i] = temp
#
#         else:
#             duplication = numbers[i]
#             break
#             # return True
# # return False
# print(duplication)
# s = "123.45e+6"
# num_dot = 0
# for i in range(len(s)):
#     if s[i] in '+-':
#         if i != 0 and s[i - 1] not in 'eE':
#             print(False)
#             break
#     elif s[i] in 'eE':
#         continue
#     elif s[i] == '.':
#         if num_dot == 1:
#             print(False)
#         else:
#             num_dot += 1
#     elif s[i].isdigit():
#         continue
#     else:
#         print(False)
# print(True)

m, n = 3, 5
children = [i for i in range(n)]
index = -1
for i in range(n - 1):
    for j in range(m):
        if index == len(children) - 1:
            index = -1
        index += 1
    del children[index]
    if index == len(children):
        index = 0
    index -= 1
print(children)