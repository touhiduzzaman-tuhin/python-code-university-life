class Square:

    def __init__(self, x):
        self.side = x

    def area(self):
        return self.side * self.side


sq1 = Square(5)

sq1.side = 6

area = sq1.area()

print(area)