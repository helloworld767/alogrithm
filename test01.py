def find(nums, target):
    begin = 0
    end = len(nums) - 1
    while begin <= end:
        mid = begin + (end - begin) // 2
        if nums[mid] == target:
            return mid
        if nums[begin] < nums[mid]:
            if nums[begin] <= target < nums[mid]:
                end = mid - 1
            else:
                begin = mid + 1
        else:
            if nums[mid] < target < nums[begin]:
                begin = mid + 1
            else:
                end = mid - 1
    return -1

nums = 
print(find(nums, target))