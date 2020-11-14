nums = [9, 4, 3, 2, 1, 0, 5, 4, 3, 2]
dp = [1 for i in range(len(nums))]
dpindex = [-1 for i in range(len(nums))]
for i in range(len(nums)):
    for j in range(i):
        if nums[i] < nums[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            dpindex[i] = j

maxlen = max(dp)
index = dp.index(maxlen)
res = []
while index != -1:
    res.append(nums[index])
    index = dpindex[index]
print(res[::-1])
