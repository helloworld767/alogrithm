nums = [1,1,1,2,2,2,3,3,3]
dp = [[1, 1] for i in range(len(nums))]
for i in range(len(nums)):
    for j in range(i):
        if nums[i] > nums[j]:
            if dp[i][0] < dp[j][0] + 1:
                dp[i] = [dp[j][0] + 1, dp[j][1]]
            elif dp[i][0] == dp[j][0] + 1:
                dp[i][1] += dp[j][1]
print(dp)