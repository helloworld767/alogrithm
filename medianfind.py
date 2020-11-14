def find_median(a, b, k):

    if not a:
        return b[k - 1]
    if not b:
        return a[k - 1]
    if k == 1:
        return min(a[0], b[0])

    num1 = a[k // 2 - 1] if k // 2 - 1 < len(a) else None
    num2 = b[k // 2 - 1] if k // 2 - 1 < len(b) else None
    if num1 and num2:
        if num1 < num2:
            return find_median(a[k // 2:], b, k - k // 2)
        elif num1 > num2:
            return find_median(a, b[k // 2:], k - k // 2)
        else:
            return num1
    elif num1:
        return find_median(a[k // 2:], b, k // 2)
    elif num2:
        return find_median(a, b[k // 2:], k // 2)


A = [1,2,3,4,5,6]
B = [2,3,4,5]

k = len(A) + len(B)
if k % 2 == 1:
    print(find_median(A, B, k // 2 + 1))
else:
    print((find_median(A, B, k // 2) + find_median(A, B, k // 2 + 1)) / 2)
