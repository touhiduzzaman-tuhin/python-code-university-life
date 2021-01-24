class A:

    def __init__(self):

        print("This is init")

    def features1(self):

        print("Features 1 Work")

    def features2(self):

        print("Features 2 Work")


class B(A):

    def features3(self):
        print("Features 3 Work")

    def features4(self):
        print("Features 4 Work")


a = A()
a.features1()
a.features2()

print("--")

b = B()

b.features1()
b.features2()
b.features3()
b.features4()

print("--")

print("-----------")

class A:

    def __init__(self):

        print("This is A init")

    def features1(self):

        print("Features 1 Work")

    def features2(self):

        print("Features 2 Work")


class B(A):

    def __init__(self):

        print("This is B init")

    def features3(self):
        print("Features 3 Work")

    def features4(self):
        print("Features 4 Work")


a = A()
a.features1()
a.features2()

print("--")

b = B()

b.features1()
b.features2()
b.features3()
b.features4()

print("--")

print("----------")

class A:

    def __init__(self):

        print("This is A init")

    def features1(self):

        print("Features 1 Work")

    def features2(self):

        print("Features 2 Work")


class B(A):

    def __init__(self):

        super().__init__()

        print("This is B init")

    def features3(self):
        print("Features 3 Work")

    def features4(self):
        print("Features 4 Work")


a = A()

print("--")

b = B()

print("--")

print("----------")

class A:

    def __init__(self):
        print("A Init")

    def fea1(self):

        print("Fea 1-A Work")

    def fea2(self):

        print("Fea @ Work")

class B:

    def __init__(self):
        print("B Init")

    def fea1(self):

        print("Fea 1-B Work")

    def fea3(self):

        print("Fea # work")

class C(A, B):

    def __init__(self):

        super().__init__()

        print("C Init")

    def fwa4(self):


        print("Fea 4 Work")


c = C()

c.fea1()