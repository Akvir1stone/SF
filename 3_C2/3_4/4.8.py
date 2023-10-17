a = input('some number:')
b = input('some number:')
c = input('some number:')
try:
    a = int(a)
    b = int(b)
    c = int(c)
except ValueError as e:
    print(e)
    print('you should have entered the numbers')
else:
    print('sum = ', a+b+c)
finally:
    print('this supposed to be here')
