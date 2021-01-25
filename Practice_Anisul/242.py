class Triangle:

    def __init__(self, base, height):

        self.base = base

        self.height = height

    def Area(self):

        area = 0.5 * self.base *self.height

        print("Arae : ", area)

x = int(input("Enter Base : "))

y = int(input("Enter Height : "))

t1 = Triangle(x, y)

t1.Area()