class Rectangle:

    def __init__(self, x, y):

        self.x = x

        self.y = y

    def arae(self):

        return self.x * self.y

r = Rectangle(10, 20)

v = r.arae()

print("Area : ", v)