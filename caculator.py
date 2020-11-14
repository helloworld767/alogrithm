def compute(s):
    if not s:
        return 0
    nums = []
    num, sign = 0, '+'
    while s:
        i = s.pop(0)
        if i == ' ':
            continue
        if i.isdigit():
            num = num * 10 + int(i)
        elif i == '(':
            num = compute(s)
        else:
            if sign == '+':
                nums.append(num)
            elif sign == '-':
                nums.append(-num)
            elif sign == '*':
                nums.append(nums.pop()*num)
            elif sign =='/':
                nums.append(nums.pop()//num)
            num = 0
            sign = i
        if sign == ')':
            break
    return sum(nums)


s = '(2+6*3+5-(3*14/7+2)*5)+3'
s = list(s)
s.append('+')
print(compute(s))

