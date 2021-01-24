class Computer:

    pass

c1 = Computer()
c2 = Computer()

print(id(c1))
print(id(c2))

print("-----")

class Student:

    def __init__(self):

        self.name = "Tuhin"
        self.age = 25

s1 = Student()
s2 = Student()

print(id(s1))
print(id(s2))

print(s1.name)
print(s2.name)

print("------")

class Student:

    def __init__(self):

        self.name = "Tuhin"
        self.age = 25

s1 = Student()
s2 = Student()


s1.name = "Touhiduzzaman"

print(s1.name)
print(s2.name)

print("-----")

class Student:

    def __init__(self):

        self.name = "Tuhin"
        self.age = 25

    def update(self):

        self.name = "Kona"

s1 = Student()
s2 = Student()

s1.update()


print(s1.name)
print(s2.name)

print("-----")

class Student:

    def __init__(self):

        self.name = "Tuhin"
        self.age = 25

    def compare(self, other):

        if self.name == other.name:

            return True

        else:

            return False


s1 = Student()
s2 = Student()

if s1.compare(s2):

    print("They Are Same")
else:

    print("They Are Not Same")

print(s1.name)
print(s2.name)

print("-------")


class Student:

    def __init__(self):

        self.name = "Tuhin"
        self.age = 25

    def compare(self, other):

        if self.name == other.name:

            return True

        else:

            return False


s1 = Student()
s2 = Student()

s1.name = "Mona"

if s1.compare(s2):

    print("They Are Same")
else:

    print("They Are Not Same")

print(s1.name)
print(s2.name)