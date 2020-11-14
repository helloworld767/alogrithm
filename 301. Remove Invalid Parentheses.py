def dfs(s):
    mistake = cal(s)
    if mistake == 0:
        return [s]
    res = []
    for i in range(len(s)):
        if s[i] not in '()':
            continue
        news = s[:i] + s[i + 1:]
        if news not in memo and cal(news) < mistake:
            memo.append(news)
            res.extend(dfs(news))
    return res


def cal(s):
    a, b = 0, 0
    for i in range(len(s)):
        if s[i] == "(":
            a += 1
        elif s[i] == ')':
            a -= 1
        b += a < 0
        a = max(a, 0)
    return a + b

s = "()())()"
memo = [s]
print(dfs(s))