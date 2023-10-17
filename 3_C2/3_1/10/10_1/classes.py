# + 1.10.2
class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def __str__(self):
        return f'Circle: center at: x = {self.x}, y = {self.y}; radius = {self.r}'

    def get_area(self):
        return self.r**2*3.14


circle = Circle(3, 2, 5)
print(circle)
print(f'Area of circle = {circle.get_area()}')
