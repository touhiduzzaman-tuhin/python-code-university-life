class Bike:

    def __init__(self, color, name):

        self.color = color

        self.name = name

    def __eq__(self, other):

        return self.name == other.name and self.color == other.color

    def display(self):

        print(f"Name : {self.name}, Color : {self.color}")

bike1= Bike("BMW", "Red")
bike2= Bike("BMW", "Red")
bike1.display()

print(bike1 == bike2)