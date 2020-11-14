list = [5,4,3,2,1]
k = 2
# dp = [[0 for i in range(len(list))] for j in range(len(list))]
# for i in range(len(list)):
#     dp[i][i] = list[i]
#
# for k in range(k - 1):
#     for i in range(len(list)):
#         for j in range(len(list) - 1, i, -1):
#             dp[i][j] = max(dp[i + 1][j] + list[i], dp[i][j - 1] + list[j])
#             print(dp)
# print(dp)
# print(max(dp[1][-1] + list[0], dp[0][-2] + list[-1]))

left = [0 for i in range(k)]
right = [0 for i in range(k)]
left[0] = list[0]
right[0] = list[-1]
for i in range(1, k):
    left[i] = left[i-1] + list[i]
    right[i] = right[i-1] + list[-i-1]
res = 0
for i in range(k+1):
    if i == 0:
        l = 0
        r = right[k-i-1]
    elif i == k:
        l = left[i-1]
        r = 0
    else:
        l = left[i-1]
        r = right[k-i-1]
    res = max(res, l+r)
    print(l, r)
print(left, right)
print(res)