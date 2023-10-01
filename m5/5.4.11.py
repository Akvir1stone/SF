def equal(N, S):
    if S < 0:
        return False
    if N < 10:
        return S == N
    return equal(N // 10, S - N % 10)


print(equal(int(input('n')), int(input('s'))))
