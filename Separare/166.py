class Square:

    side = 0

    def area(self):
        return self.side * self.side


sq1 = Square()

sq1.side = 6

area = sq1.area()

print(area)