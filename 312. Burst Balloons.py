def dfs(nums):
    if len(nums) == 1:
        return nums[0]
    t = tuple(nums)
    if t in dp:
        return dp[t]
    res = 0
    for i in range(len(nums)):
        s = dfs(nums[:i] + nums[i + 1:])
        if i == 0:
            s = s + nums[0] * nums[1]
        elif i == len(nums) - 1:
            s = s + nums[-1] * nums[-2]
        else:
            s = s + nums[i - 1] * nums[i] * nums[i + 1]
        res = max(res, s)
    dp[t] = res
    return res


# dp = {}
# nums = [8,3,4,3,5,0,5,6,6,2,8,5,6,2,3,8,3,5,1,0,2]
# print(dfs(nums))
nums = [3,1,5,8]

nums = [1] + nums + [1]
dp = [[0] * len(nums) for i in range(len(nums))]

for gap in range(2, len(nums)):
    for i in range(0, len(nums) - gap):
        j = i + gap
        for k in range(i + 1, j):
            dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j])
            print(dp)
print(dp[0][len(nums) - 1])