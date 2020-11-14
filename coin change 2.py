dp = {}
amount = 5
coins = [1,2,5]
a = []

def search(k, amount, coins, subset):
    if amount == 0:
        a.append(subset)
        return 1
    # if amount in dp:
    #     return dp[amount]
    res = 0
    for i in range(k, len(coins)):
        if amount - coins[i] >= 0:
            res += search(i, amount-coins[i], coins, subset+[coins[i]])
    # dp[amount] = res
    return res


print(search(0, amount, coins, []))
print(dp)
print(a)