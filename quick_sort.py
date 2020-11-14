def mergesort(nums):
    if len(nums) < 2:
        return
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]
    mergesort(left)
    mergesort(right)
    nums.clear()
    merge(left, right, nums)


def merge(l, r, nums):
    i, j = 0, 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            nums.append(l[i])
            i += 1
        else:
            nums.append(r[j])
            j += 1
    if i < len(l):
        nums.extend(l[i:])
    elif j < len(r):
        nums.extend(r[j:])


def quick_sort(nums, left, right):
    if left >= right:
        return
    mid = nums[left]
    l, r = left, right
    while l < r:
        while l < r and nums[r] >= mid:
            r -= 1
        nums[l] = nums[r]
        while l < r and nums[l] < mid:
            l += 1
        nums[r] = nums[l]
    nums[l] = mid
    quick_sort(nums, left, l-1)
    quick_sort(nums, l+1, right)


if __name__ == "__main__":
    li = [5, 7, 9, 8, 2, 4, 1, 3, 6, 4, 9, 3, 1]
    # mergesort(li)
    quick_sort(li, 0, len(li) - 1)
    print(li)
