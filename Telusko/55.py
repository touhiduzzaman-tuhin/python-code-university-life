class A:

    def features1(self):

        print("Features 1 Work")

    def features2(self):

        print("Features 2 Work")

a = A()

a.features1()
a.features2()

print("----")

class B:

    def features3(self):
        print("Features 3 Work")

    def features4(self):
        print("Features 4 Work")


b = B()

b.features3()
b.features4()

print("---------------")

class A:

    def features1(self):

        print("Features 1 Work")

    def features2(self):

        print("Features 2 Work")

a = A()

a.features1()
a.features2()

print("----")

class B(A):

    def features3(self):
        print("Features 3 Work")

    def features4(self):
        print("Features 4 Work")


b = B()

b.features1()
b.features2()
b.features3()
b.features4()

print("---------------")

class A:

    def features1(self):

        print("Features 1 Work")

    def features2(self):

        print("Features 2 Work")

a = A()

a.features1()
a.features2()

print("----")

class B(A):

    def features3(self):
        print("Features 3 Work")

    def features4(self):
        print("Features 4 Work")


class C(B):

    def features5(self):

        print("Features 5 work")


c = C()
c.features1()
c.features2()
c.features3()
c.features4()
c.features5()

print("---------------")

class A:

    def features1(self):

        print("Features 1 Work")

    def features2(self):

        print("Features 2 Work")

a = A()

a.features1()
a.features2()

print("----")

class B():

    def features3(self):
        print("Features 3 Work")

    def features4(self):
        print("Features 4 Work")


class C(A, B):

    def features5(self):

        print("Features 5 work")


c = C()
c.features1()
c.features2()
c.features3()
c.features4()
c.features5()