class Shape:

    def __init__(self, dim1, dim2):

        self.dim1 = dim1

        self.dim2 = dim2

    def area(self):

        print("Shape Class")

class Triangle(Shape):

    def area(self):

        area = 0.5 * self.dim1 * self.dim2

        print("Area = ", area)

class Rectangle(Shape):

    def area(self):

        area = self.dim1 * self.dim2

        print("Area = ", area)

t1 = Triangle(20, 30)
t1.area()

print("\n")

r1 = Rectangle(20, 30)
r1.area()