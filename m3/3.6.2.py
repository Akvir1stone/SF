P = 1  # заводим переменную-счётчик, в которой мы будем считать произведение, подумайте, чему она должна быть равна
N = 5

# запишите цикл for для подсчёта произведения
for i in range(1, N + 1):
    P *= i
print(P)
