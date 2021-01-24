class Student:

    name = ""
    id = ""

    def set_value(self, name, id):

        self.name = name

        self.id = id

    def display(self):

        print(f"Name : {self.name}, Id : {self.id}")

s1 = Student()
s1.set_value("Shahed", 102)
s1.display()