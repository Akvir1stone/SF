def repeater(list_):
    list_values = list_.copy()
    while True:
        value = list_values.pop(0)
        list_values.append(value)
        yield value


count = 0
for i in repeater([1,2,3]):
    count += 1
    if count == 10:
        break
    print(i)
