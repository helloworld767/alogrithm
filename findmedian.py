def findk(nums1, l1, r1, nums2, l2, r2, k):

    m = r1 - l1 + 1
    n = r2 - l2 + 1
    if m > n:
        return findk(nums2, l2, r2, nums1, l1, r1, k)

    if m == 0:
        return nums2[l2 + k - 1]
    if k == 1:
        return min(nums1[l1], nums2[l2])

    n1 = min(m, k // 2)
    n2 = k - n1
    if nums1[l1 + n1 - 1] == nums2[l2 + n2 - 1]:
        return nums1[l1 + n1 - 1]
    elif nums1[l1 + n1 - 1] > nums2[l2 + n2 - 1]:
        return findk(nums1, l1, l1 + n1 - 1, nums2, l2 + n2, r2, k - n2)
    else:
        return findk(nums1, l1 + n1, r1, nums2, l2, l2 + n2 - 1, k - n1)


nums1 = [1]
nums2 = [2,3,4,5,6]
n1 = len(nums1)
n2 = len(nums2)
k = (n1 + n2) // 2
if (n1 + n2) % 2 == 0:
    k1 = findk(nums1, 0, n1 - 1, nums2, 0, n2 - 1, k)
    k2 = findk(nums1, 0, n1 - 1, nums2, 0, n2 - 1, k + 1)
    print((k1 + k2) / 2)
else:
    print(findk(nums1, 0, n1 - 1, nums2, 0, n2 - 1, k+1))