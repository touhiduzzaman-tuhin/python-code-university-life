class Square:

    def area(self):
        return self.side * self.side


sq1 = Square()

sq1.side = 7

area = sq1.area()

print(area)