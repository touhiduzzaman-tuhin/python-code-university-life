class Square:

    def __init__(self):
        self.side = 5

    def area(self):
        return self.side * self.side


sq1 = Square()

area = sq1.area()

print(area)