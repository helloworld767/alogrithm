def quick_select(nums, left, right, k):
    if left > right:
        return
    flag = nums[left]
    l, r = left, right
    while l < r:
        while l < r and nums[r] >= flag:
            r -= 1
        nums[l] = nums[r]
        while l < r and nums[l] < flag:
            l += 1
        nums[r] = nums[l]
    nums[r] = flag
    if r == k - 1:
        return flag
    elif r > k - 1:
        return quick_select(nums, left, r - 1, k)
    else:
        return quick_select(nums, r + 1, right, k)



nums = [3,2,1,5,6,4]
k = 2
print(quick_select(nums, 0, len(nums) - 1, len(nums) - k))
