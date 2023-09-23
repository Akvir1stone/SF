import time


def decorator_time(fn):
    def wrapper():
        # print(f"Запустилась функция {fn}")
        t0 = time.time()
        result = fn()
        dt = time.time() - t0
        # print(f"Функция выполнилась. Время: {dt:.10f}")
        return dt  # задекорированная функция будет возвращать время работы
    return wrapper


def pow_2():
    return 10000000 ** 20000


def in_build_pow():
    return pow(10000000, 20000)


def average_time(fun):
    sumt = 0
    fun = decorator_time(fun)
    for i in range(100):
        sumt += fun()
    return sumt/100


print(average_time(pow_2))
print(average_time(in_build_pow))
