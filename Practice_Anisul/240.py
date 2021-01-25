class Student:

    name = ""
    id = ""

    def __init__(self, name, id):

        self.name = name

        self.id = id

    def display(self):

        print(f"Name: {self.name}, Id : {self.id}")


s1 = Student("Tuhin", 101)
s1.display()