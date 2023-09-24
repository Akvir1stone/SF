def suml(n):
    sumn = 0
    if n == 1:
        return 1
    if n == 0:
        return 0
    return n + suml(n-1)


print(suml(int(input('n = '))))
