class Car:

    def __init__(self):

        self.name = "BMW"
        self.mils = 10

c1 = Car()
c2 = Car()


print(c1.name, c1.mils)
print(c2.name, c2.mils)

print("----------")

class Car:

    def __init__(self):

        self.name = "BMW"
        self.mils = 10

c1 = Car()
c2 = Car()

c1.mils = 12


print(c1.name, c1.mils)
print(c2.name, c2.mils)

print("---")

class Car:

    wheel = 4

    def __init__(self):

        self.name = "BMW"
        self.mils = 10

c1 = Car()
c2 = Car()


print(c1.name, c1.mils, c1.wheel)
print(c2.name, c2.mils, c2.wheel)

print("---")

class Car:

    wheel = 4

    def __init__(self):

        self.name = "BMW"
        self.mils = 10

c1 = Car()
c2 = Car()

c1.wheel = 5


print(c1.name, c1.mils, c1.wheel)
print(c2.name, c2.mils, c2.wheel)

print("----")

print("---")

class Car:

    wheel = 4

    def __init__(self):

        self.name = "BMW"
        self.mils = 10

c1 = Car()
c2 = Car()

Car.wheel = 6

print(c1.name, c1.mils, c1.wheel)
print(c2.name, c2.mils, c2.wheel)