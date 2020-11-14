# memo = dict()
#
#
# def dp(K, N):
#     if K == 1: return N
#     if N == 0: return 0
#     if (K, N) in memo:
#         return memo[(K, N)]
#
#
#     lo, hi = 1, N
#     while lo <= hi:
#         mid = (lo + hi) // 2
#         broken = dp(K - 1, mid - 1)  # 碎
#         not_broken = dp(K, N - mid)  # 没碎
#         # res = min(max(碎，没碎) + 1)
#         if broken > not_broken:
#             hi = mid - 1
#             res = min(res, broken + 1)
#         else:
#             lo = mid + 1
#             res = min(res, not_broken + 1)
#
#     memo[(K, N)] = res
#     return res
#
#
#
#
# K, N = 2, 6
# print(dp(K, N))

n = 10000007
dp = [[0 for i in range(n + 1)] for j in range(3)]
m = 0
while dp[2][m] < n:
    m += 1
    for k in range(1, 3):
        dp[k][m] = dp[k - 1][m - 1] + dp[k][m - 1] + 1
print(m)