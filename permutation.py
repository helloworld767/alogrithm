def permutation(nums, subset, res):
    if not nums:
        res.append(subset.copy())
    for i in range(len(nums)):
        permutation(nums[: i] + nums[i + 1:], subset + [nums[i]], res)
    return


n = 4
nums = [i for i in range(1, n + 1)]
res = []
permutation(nums, [], res)
for list in res:
    print(list)
