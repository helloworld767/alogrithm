def dfs(k, days, costs):
    print(k)
    if k >= len(days):
        return 0
    if k in dp:
        return dp[k]
    res = float('inf')
    for i in range(len(costs)):
        if i == 0:
            res = min(res, dfs(k+1, days, costs)+costs[0])
        elif i == 1:
            j = k
            while j < len(days):
                if days[j] - days[k] >= 7:
                    break
                j += 1
            res = min(res, dfs(j, days, costs) + costs[1])
        elif i == 2:
            j = k
            while j < len(days):
                if days[j] - days[k] >= 30:
                    break
                j += 1
            res = min(res, dfs(j, days, costs) + costs[2])
    dp[k] = res
    return res


dp = {}
days = [1,4,6,7,8,20]
costs = [2,7,15]
print(dfs(0, days, costs))
