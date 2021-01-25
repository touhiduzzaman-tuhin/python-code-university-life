class Square:

    def __init__(self):

        self.side = 0

    def area(self):

        return self.side * self.side

s = Square()

s.side = 8

area = s.area()

print("Area = ", area)