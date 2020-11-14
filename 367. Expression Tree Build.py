expression = ["2","*","6","-","(","23","+","7",")","/","(","1","+","2",")"]
preorder = []
op = []
for i in range(len(expression) - 1, -1, -1):
    if expression[i].isdigit():
        preorder.append(expression[i])
    elif expression[i] == ')':
        op.append(expression[i])
    elif expression[i] == '(':
        while op[-1] != ')':
            preorder.append(op.pop())
        op.pop()
    else:
        if expression[i] in '*/':
            op.append(expression[i])
        else:
            while op and op[-1] in '*/':
                preorder.append(op.pop())
            op.append(expression[i])
print(preorder[::-1])
