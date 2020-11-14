def dfs(i, k, stones):
    if i == len(stones) - 1:
        return True
    if (i, k) in dp:
        print(i, k)
        return False
    if (k + stones[i]) in stones[i + 1:] and dfs(stones.index(k + stones[i]), k, stones):
        return True
    if (k + 1 + stones[i]) in stones[i + 1:] and dfs(stones.index(k + 1 + stones[i]), k + 1, stones):
        return True
    if (k - 1 + stones[i]) in stones[i + 1:] and dfs(stones.index(k - 1 + stones[i]), k - 1, stones):
        return True
    dp.add((i, k))
    return False

