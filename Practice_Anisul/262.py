class A:

    def display(self):

        print("A Class")

class B:

    def display(self):

        print("B Class")

class C(A, B):

    pass

c = C()
c.display()