def draw_stairs(steps):
    for i in range(1, steps + 1):
        print('*' * i)


draw_stairs(int(input('how much steps ')))
