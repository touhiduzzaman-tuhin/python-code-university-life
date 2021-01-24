class Car:

    def __init__(self, name, model):

        self.name = name

        self.model = model

    def display(self):

        print(f"Name : {self.name}, MOdel : {self.model}")

c = Car('BMW', 'R8')
c.display()