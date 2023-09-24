def dec(fun):
    dictin = {}

    def wrap(arg):
        nonlocal dictin
        if arg not in dictin:
            dictin[arg] = fun(arg)
            print(dictin)
        else:
            print(dictin)
    return wrap


@dec
def mult5(n):
    return n*5


mult5(3)
mult5(2)
mult5(23)
mult5(7)
mult5(7)
mult5(7)
mult5(7)
