def dev_count(a):
    count = 0
    for i in range(1, a+1):
        if a % i == 0:
            count += 1
    return count


print(dev_count(int(input('write number '))))
