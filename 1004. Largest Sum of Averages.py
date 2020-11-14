def dfs(A, K):
    if K == 1:
        return sum(A) / len(A)
    if len(A) == K:
        return sum(A)
    average_sum = 0
    for i in range(len(A) - K + 1):
        average = sum(A[:i + 1]) / (i + 1)
        average_sum = max(average_sum, dfs(A[i + 1:], K - 1) + average)

    return average_sum

A = [9,1,2,3,9]
K = 3
print(dfs(A, K))