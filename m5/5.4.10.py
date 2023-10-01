def mirr(i, res):
    return mirr(i // 10, res * 10 + i % 10) if i else res


