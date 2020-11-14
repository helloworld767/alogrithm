l = [5, 0, 0]
def hano(a, b, c, n):
    if n > 0:
        hano(a, c, b, n-1)
        l[a] -= 1
        l[c] += 1
        print(l)
        hano(b, a, c, n-1)

hano(0, 1, 2, 5)
print(l)