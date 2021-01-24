class Square:

    def __init__(self):
        self.side = 0

    def area(self):

        return self.side * self.side

sq1 = Square()
area = sq1.area()
print(area)


class Square:

    def __init__(self, x):
        self.side = x

    def area(self):
        return self.side * self.side


sq1 = Square(4)
area = sq1.area()
print(area)


class Square:

    def __init__(self, x):
        self.side = x

    def area(self):
        return self.side * self.side


sq1 = Square(4)
sq1.side = 6
area = sq1.area()
print(area)