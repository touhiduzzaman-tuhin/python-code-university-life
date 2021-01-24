class Car:

    def __init__(self, x, y):

        self.x = x

        self.y = y

    def display(self):

        print(f"Name : {self.x}, Model : {self.y}")

c = Car('BMW', 10)

c1 = Car('RMW', 20)

c.display()

c1.display()