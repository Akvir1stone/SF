def draw_stairs(steps):
    for i in range(steps, 0, -1):
        print('*' * i)


draw_stairs(int(input('how much steps ')))
