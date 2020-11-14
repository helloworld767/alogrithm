import collections
n = 2
m = 3
limit = 2
cost = [0,1,1]
dpnum = [collections.defaultdict(int) for i in range(n + 1)]
dp = collections.defaultdict(set)
dp[0].add(m)
dpnum[0][m] = 1
for i in range(n + 1):
    for step in range(1, limit + 1):
        for money in dp[i]:
            if step + i < len(cost) and money - cost[step + i] >= 0:
                dp[i + step].add(money - cost[step + i])
                dpnum[i + step][money - cost[step + i]] += dpnum[i][money]
print(sum(dpnum[-1].values()))


