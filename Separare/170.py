class Square:

    def __init__(self, x):
        self.side = x

    def area(self):
        return self.side * self.side


sq1 = Square(9)

area = sq1.area()

print(area)