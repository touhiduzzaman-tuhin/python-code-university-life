class Triangle:

    def __init__(self, x, y):

        self.x = x

        self.y = y

    def arae(self):

        return 0.5 * self.x * self.y

t = Triangle(10, 20)

v = t.arae()

print("Area : ", v)