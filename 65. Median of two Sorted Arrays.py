def findMedian(a, begin1, end1, b, begin2, end2):
    mid1 = begin1 + (end1 - begin1) // 2
    mid2 = begin2 + (end2 - begin2) // 2
    if begin1 > end1 and begin2 <= end2:
        return b[mid2]
    elif begin2 > end2 and begin1 <= end1:
        return a[mid1]

    if a[mid1] < b[mid2]:
        if mid1 + 1 > end1 and begin2 > mid2 - 1:
            return min(a[mid1], b[mid2])
        return findMedian(a, mid1 + 1, end1, b, begin2, mid2 - 1)
    elif a[mid1] > b[mid2]:
        if begin1 > mid1 - 1 and mid2 + 1 > end2:
            return min(a[mid1], b[mid2])
        return findMedian(a, begin1, mid1 - 1, b, mid2 + 1, end2)
    else:
        return a[mid1]


A = [5,6,9,10]
B = [2,3, 4]
print(findMedian(A, 0, len(A) - 1, B, 0, len(B) - 1))