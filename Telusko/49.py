
a = "6"

print(type(a))

print("----")

a = 9

print(type(a))

print("------")

class Computer:

    def config(self):

        print("This is config 1")

com1 = Computer()
com2 = Computer()

print(type(com1))

print("---")

Computer.config(com1)
Computer.config(com2)

print("----")

com1.config()
com2.config()