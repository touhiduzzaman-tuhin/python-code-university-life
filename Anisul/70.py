class A:

    def display1(self):

        print("A Class")

class B(A):

    #dispaly1()
    #dispaly2()

    def display2(self):

        print("B Class")

class C(B):

    #display1()
    #display2()
    #display3()

    def display3(self):

        print("C Class")

c = C()
c.display1()
c.display2()
c.display3()