import random


def qsort(array, left, right):
    p = random.choice(array[left: right+1])
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)
