class Square:

    side = 0

    def area(self):

        return self.side * self.side

s = Square()

s.side = 6

area = s.area()

print("Area = ", area)