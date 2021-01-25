class Square:

    def __init__(self):

        print("Square")

    def area(self, x, y):

        return self.x * self.y

class Rectangle(Square):

    pass

s = Square()

r = Rectangle()

print(s)
print(r)