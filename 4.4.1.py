def natnum(b=1, s=1):
    count = b
    while True:
        yield count
        count += s


for n in natnum():
    if n == 50:
        break
    print(n)
