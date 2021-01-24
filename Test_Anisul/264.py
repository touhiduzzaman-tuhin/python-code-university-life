from abc import ABC, abstractmethod

class A(ABC):

    @abstractmethod
    def display(self):

        pass

class B(A):

    def display(self):

        print("B Class")

class C(B):

    def display1(self):
        print("C Class")



#a = A()

b = B()

b.display()

c = C()
c.display()
c.display1()