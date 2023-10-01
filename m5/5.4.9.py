def minl(L):
    if len(L) == 1:
        return L[0]
    return L[0] if L[0] < minl(L[1:]) else minl(L[1:])

