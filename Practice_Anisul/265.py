from abc import ABC, abstractmethod

class Shape(ABC):

    def __init__(self, x, y):

        self.x = x

        self.y = y

    @abstractmethod

    def area(self):

        pass

class Triangle(Shape):

    def area(self):

        area = 0.5 * self.x * self.y

        print("Triangle Area : ", area)

class Rectabgle(Shape):

    def area(self):

        area = self.x * self.y

        print("Rectangle Area : ", area)



t = Triangle(10, 20)
t.area()

print("---")

r = Rectabgle(10, 20)
r.area()