class Student:

    def sum(self, a, b):

        s = a + b

        return s



s1 = Student()

print(s1.sum(10, 20))

print("----")

class Student:

    def sum(self, a, b, c):

        s = a + b + c

        return s



s1 = Student()

print(s1.sum(10, 20, 30))


print("----")

class Student:

    def sum(self, a=None, b=None, c=None):

        if a != None and b != None and c != None:

            s = a + b + c

        elif a != None and b != None:

            s = a + b

        else:

            s = a

        return s



s1 = Student()

print(s1.sum(10, 20))

print("-----")

class A:

    def show(self):

        print("A Class")

class B:

    pass


a = A()
a.show()

b = B()

print("---")


class A:

    def show(self):

        print("A Class")

class B(A):

    pass


a = A()
a.show()

b = B()
b.show()

print("----")


class A:

    def show(self):

        print("A Class")

class B(A):

    def show(self):

        print("B Class")



a = A()
a.show()

b = B()
b.show()