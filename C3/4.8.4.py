def sort(line: list):
    count = 0
    for i in range(len(line)):
        hd = line[i]
        j = 0
        while hd < line[i - j - 1]:
            count += 1
            if i - j - 1 != -1:
                count += 1
                line[i - j] = line[i - j - 1]
            else:
                break
            j += 1
        line[i - j] = hd
    return line, count


print(sort([2, 3, 1, 4, 6, 5, 9, 8, 7]))
