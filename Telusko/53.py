class Student:

    school = 'DIU'

    def __init__(self, m1, m2, m3):

        self.m1 = m1

        self.m2 = m2

        self.m3 = m3

    def avg(self):

        return (self.m1 + self.m2 + self.m3) / 3


s1 = Student(10, 90, 60)
s2 = Student(80, 40, 12)

print(s1.avg())

print(s2.avg())


print("------")

class Student:

    school = 'DIU'

    def __init__(self, m1, m2, m3):

        self.m1 = m1

        self.m2 = m2

        self.m3 = m3


    def get_value(self):

        return self.m1

    def set_value(self, value):

        self.m1 = value


s1 = Student(10, 90, 60)
s2 = Student(80, 40, 12)

s1.set_value(90)

print(s1.get_value())

print(s2.get_value())

print("--------")

class Student:

    school = 'DIU'

    def __init__(self, m1, m2, m3):

        self.m1 = m1

        self.m2 = m2

        self.m3 = m3

    @classmethod
    def info(cls):

        return cls.school




s1 = Student(10, 90, 60)
s2 = Student(80, 40, 12)

print(s1.info())

print(Student.info())

print("----")

class Student:


    @staticmethod
    def get_classname():

        print("This is a abcd Class")

s1 = Student()

Student.get_classname()