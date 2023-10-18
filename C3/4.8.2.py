array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
count = 0
for i in range(len(array)):
    idx_min = i
    for j in range(i+1, len(array)):
        count += 1
        if array[j] > array[idx_min]:
            idx_min = j

    if i != idx_min:
        array[i], array[idx_min] = array[idx_min], array[i]


print(array)
print(count)
