class Shape:

    def __init__(self, x, y):

        self.x = x

        self.y = y

    def area(self):

        print("This is Shape Class")

class Triangle(Shape):

    def area(self):

        area = 0.5 * self.x * self.y

        print("Triangle Area : ", area)

class Rectabgle(Shape):

    def area(self):

        area = self.x * self.y

        print("Rectangle Area : ", area)

s = Shape(10, 20)
s.area()

print("---")

t = Triangle(10, 20)
t.area()

print("---")

r = Rectabgle(10, 20)
r.area()