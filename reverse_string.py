def findMedian(a, begin1, end1, b, begin2, end2):
    mid1 = begin1 + (end1 - begin1) // 2
    mid2 = begin2 + (end2 - begin2) // 2
    if begin1 > end1 and begin2 <= end2:
        if (end2 - begin2 + 1) % 2 == 1:
            return b[mid2]
        else:
            return (b[mid2] + b[mid2 + 1]) / 2
    elif begin2 > end2 and begin1 <= end1:
        if (end1 - begin1 + 1) % 2 == 1:
            return a[mid1]
        else:
            return (a[mid1] + a[mid1 + 1]) / 2
        return a[mid1]
    else:
        return False
    if a[mid1] < b[mid2]:
        res = findMedian(a, mid1 + 1, end1, b, begin2, mid2 - 1)
        if not res:
            return (a[mid1] + b[mid2]) // 2
        return res
    elif a[mid1] > b[mid2]:
        res = findMedian(a, begin1, mid1 - 1, b, mid2 + 1, end2)
        if not res:
            return (a[mid1] + b[mid2]) // 2
        return res
    else:
        if (end1 - begin1 + 1) % 2 == 0 and (end2 - begin2 + 1) % 2 == 0:
            if a[mid1 + 1] < b[mid2 + 1]:
                return (a[mid1] + a[mid1 + 1]) / 2
            else:
                return (a[mid1] + b[mid2 + 1]) / 2
        else:
            return a[mid1]


