class Square:

    def __init__(self, x):

        self.side = x

    def area(self):

        return self.side * self.side

s = Square(8)

s.side = 5

area = s.area()

print("Area = ", area)