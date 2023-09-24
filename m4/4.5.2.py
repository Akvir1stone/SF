def dec(fun):
    count = 0

    def wrap(*args):
        nonlocal count
        fun(*args)
        count += 1
        print(count)
    return wrap


@dec
def hi():
    print('hi')


hi()
hi()
hi()
