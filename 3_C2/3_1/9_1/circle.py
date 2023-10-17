class Circle:
    def __init__(self, r):
        self.r = r

    def get_area(self):
        return self.r**2*3.14


circle1 = Circle(4)
print(circle1.get_area())
