class Square:

    def __init__(self, x):

        self.side = x

    def area(self):

        return self.side * self.side

s = Square(6)

s.side = 7

print(s.side)

print(s.area())

print(Square.area(s))