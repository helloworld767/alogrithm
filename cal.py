def compute(s):
    nums = []
    num = 0
    sign = '+'
    for i in range(len(s)):
        if s[i].isdigit():
            num = num * 10 + int(s[i])
        elif s[i] == '(':
            num = compute(s[i + 1:])
        elif s[i] == ' ':
            continue
        else:
            if sign == '+':
                nums.append(num)
            elif sign == '-':
                nums.append(-num)
            elif sign == '/':
                nums.append(nums.pop() // num)
            elif sign == '*':
                nums.append(nums.pop() * num)
            sign = s[i]
            num = 0
            if s[i] == ')':
                return sum(nums)
    return sum(nums)


s = "2*(5+5*2)/3+(6/2+8)"
s = list(s)
s.append('+')
print(compute(s))
