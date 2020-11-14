def merge(nums):
    if len(nums) == 0:
        return
    if len(nums) == 1:
        return nums
    if len(nums) == 2:
        return mergeTwo([nums[0]], [nums[1]])
    mid = len(nums) // 2
    l = nums[:mid]
    r = nums[mid:]
    l = merge(l)
    r = merge(r)
    return mergeTwo(l, r)


def mergeTwo(l, r):
    i, j = 0, 0
    res = []
    while i < len(l) and j < len(r):
        if l[i] > r[j]:
            res.append(r[j])
            j += 1
        else:
            res.append(l[i])
            i += 1
    if i < len(l):
        res.extend(l[i:])
    elif j < len(r):
        res.extend(r[j:])
    return res

nums = [2,0,2,1,1,0]
nums = merge(nums)
print(nums)