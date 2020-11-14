A = [18,85,96,61,49,90,33,68,59,27,0,46,19,63,94,21,57,31,3,62,99,25,23,37,82,11,9,73,35,80,24,69,72,34,77,39,12,88,42,60,55,67,97,45,50,51,65,36,6,20,47,84,58,28,41,93,14,7,78,86,81,13,89,76,30,74,22,2,48,53,43,40,79,64,92,5,75,44,8,66]
count = 1
res = 0
state = 0
for i in range(1, len(A)):

    if state == 0:
        if A[i] > A[i - 1]:
            state == 1
        elif A[i] < A[i - 1]:
            state = -1
        else:
            continue
        count += 1
    elif state == 1:
        if A[i] > A[i - 1]:
            count += 1
        elif A[i] < A[i - 1]:
            state = -1
            res = max(res, count)
            count =2
        else:
            state = 0
            res = max(res, count)
            count =1
    elif state == -1:
        if A[i] < A[i - 1]:
            count += 1
        elif A[i] > A[i - 1]:
            state = 1
            res = max(res, count)
            count = 2
        else:
            state = 0
            res = max(res, count)
            count = 2
print(max(count, res))