class Student:

    def __init__(self, name, roll):

        self.name = name

        self.roll = roll


s1 = Student('Tuhin', 3)
s2 = Student('Rana', 5)

print(s1.name, s1.roll)
print(s2.name, s2.roll)

print("----")

class Student:

    def __init__(self, name, roll):

        self.name = name

        self.roll = roll

    def show(self):

        print(self.name, self.roll)


s1 = Student('Tuhin', 3)
s2 = Student('Rana', 5)

s1.show()
s2.show()

print("------")

class Student:

    def __init__(self, name, roll):

        self.name = name

        self.roll = roll


s1 = Student('Tuhin', 3)
s2 = Student('Rana', 5)

print(s1.name, s1.roll)
print(s2.name, s2.roll)

print("----")


class Student:

    def __init__(self, name, roll, brand, cpu, ram):
        self.name = name

        self.roll = roll

        self.brand = brand

        self.cpu = cpu

        self.ram = ram

    def show(self):
        print(self.name, self.roll, self.brand, self.cpu, self.ram)


s1 = Student('Tuhin', 3, 'Hp', 'i5', 8)
s2 = Student('Rana', 5, 'Hp', 'i7', 8)

s1.show()
s2.show()


print("-----")

class Student:

    def __init__(self, name, roll):

        self.name = name

        self.roll = roll

        self.lap = self.Laptop()

    class Laptop:

        def __init__(self):

            self.brand = 'Hp'

            self.cpu = 'i7'

            self.ram = 16


s1 = Student('Tuhin', 3)
s2 = Student('Rana', 5)

print(s1.name, s1.roll)

print(s1.lap.brand)

lap1 = s1.lap
lap2 = s2.lap

print(lap1.ram)

print("---")

print(id(lap1))
print(id(lap2))

print("-----")

l1 = Student.Laptop()

print(l1.cpu)

print("-----")

class Student:

    def __init__(self, name, roll):

        self.name = name

        self.roll = roll

        self.lap = self.Laptop()

    def show(self):

        print(self.name, self.roll)

        self.lap.show()


    class Laptop:

        def __init__(self):

            self.brand = 'Hp'

            self.cpu = 'i7'

            self.ram = 16

        def show(self):

            print(self.brand, self.cpu, self.ram)


s1 = Student('Tuhin', 3)
s2 = Student('Rana', 5)

s1.show()