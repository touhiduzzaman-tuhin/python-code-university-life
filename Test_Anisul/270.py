class Car:

    def __init__(self, x, y):

        self.x = x

        self.y = y

    def __eq__(self, other):

        return self.x == other.x


c = Car('BMW', 10)

c1 = Car('BMW', 20)

print(c == c1)