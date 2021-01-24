class Student:

    def __init__(self, name, age):

        self.name = name

        self.age = age

    def about(self):

        print("Name: ", self.name, "Age : ", self.age)

s1 = Student('Tuhin', 25)

s2 = Student('Rana', 28)


s1.about()

s2.about()