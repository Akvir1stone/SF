def par_checker(string):
    stack = {'(': 0, '[': 0, ')': 0, ']': 0}

    for s in string:  # читаем строку посимвольно
        if s in stack.keys():  # если открывающая скобка,
            stack[s] += 1  # добавляем её в стек
    if stack['('] - stack[')'] == 0 and stack['['] - stack[']'] == 0:
        return True
    else:
        return False


print(par_checker('[(5+6)*(7+8)/(4+3)'))
