class Rectangle:

    def __init__(self, x, y):

        self.x = x

        self.y = y

    def arae(self):

        print("Area : ", self.x * self.y)

r = Rectangle(10, 20)
r.arae()