# def ismatch(s, i, p, j):
#     if j == len(p):
#         return i == len(s)
#     if j == len(p) - 1 or p[j + 1] != '*':
#         return i < len(s) and (p[j] == s[i] or p[j] == '.') and ismatch(s, i + 1, p, j + 1)
#     if j < len(p) - 1 and p[j + 1] == '*':
#         while i < len(s) and (s[i] == p[j] or p[j] == '.'):
#             if ismatch(s, i+1, p, j + 2):
#                 return True
#             i += 1
#     return False
#
#
# s = "aa"
# p = "a*"
# print(ismatch(s, 0, p, 0))

s = "aa"
p = "*"
dp = [[False for i in range(len(s) + 1)] for j in range(len(p) + 1)]
dp[0][0] = True
if p[0] == '*':
    dp[1][0] = True
for i in range(1, len(p) + 1):
    for j in range(1, len(s) + 1):
        if p[i - 1] == s[j - 1] or p[i - 1] == '?':
            dp[i][j] = dp[i - 1][j - 1]
        elif p[i - 1] == '?':
            dp[i][j] = dp[i-1][j] or dp[i][j - 1] or dp[i - 1][j - 1]
print(dp)
