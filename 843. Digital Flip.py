import collections


def dfs(i, nums):
    if i == len(nums):
        return 0
    if nums[i] == 0:
        count0 = 1
        count1 = dic[i]
        while i < len(nums) - 1 and nums[i + 1] == 0:
            i += 1
            count0 += 1
        return min(count1, dfs(i + 1, nums) + count0)
    else:
        return dfs(i + 1, nums)


nums = [0,1,1,1,0,0,1,1,1,0]
count1 = 0
dic = collections.defaultdict(int)
for i in range(len(nums)-1, -1, -1):
    if nums[i] == 1:
        count1 += 1
    dic[i] = count1
print(dfs(0, nums))
