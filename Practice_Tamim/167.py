class Square:

    def __init__(self):

        print("Square")

    def area(self, x, y):

        return self.x * self.y

class Rectangle(Square):

    def __init__(self):

        print("Rectangle")

    def area(self, x):

        return self.x * self.x

s = Square()

r = Rectangle()



print(s.area(4, 5))
print(r.area(9))