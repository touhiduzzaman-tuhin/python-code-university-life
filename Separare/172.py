class Square:

    side = 3

    def __init__(self, x):

        self.side = x

    def area(self):

        return self.side * self.side

sq1 = Square(6)

print(sq1.side)

print(Square.area(sq1))

print(sq1.area())