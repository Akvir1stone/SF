class Square:
    def __init__(self, a):
        self.side = a

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        if int(value) >= 0:
            self._side = int(value)
        else:
            raise ValueError("Side can't be lesser than 0")

    @property
    def area(self):
        return self.side**2


class SquareFactory:
    @staticmethod
    def cSquare(a):
        return Square(a)


s = Square(3)
#s.side = input('side: ')
print(s.area)
