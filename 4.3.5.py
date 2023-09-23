def sumn(N):
    if N % 10 == 0:
        return N
    return N % 10 + sumn(N // 10)


print(sumn(int(input('n = '))))
