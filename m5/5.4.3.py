def discr(a, b, c):
    return b**2 - 4*a*c


def quadratic_solve(a, b, c):
    if discr(a, b, c) < 0:
        return 'NO'
    elif discr(a, b, c) == 0:
        return -b/(2*a)
    else:
        return (-b - discr(a, b, c) ** 0.5) / (2 * a), (-b + discr(a, b, c) ** 0.5) / (2 * a)
