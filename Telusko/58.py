a = 5

b = 6

print(a + b)

print(int.__add__(a, b))
print(int.__sub__(a, b))
print(int.__mul__(a, b))
print(int.__mod__(a, b))


print("----")

a = '7'

b = 'Tuhin'

print(a + b)

print(str.__add__(a, b))


print("----")
class Student:

    def __init__(self, m1, m2):

        self.m1 = m1

        self.m2 = m2

    def __add__(self, other):

        m1 = self.m1 + other.m1

        m2 = self.m2 + other.m2

        m3 = Student(m1, m2)

        return m3



s1 = Student(60, 80)
s2 = Student(70, 96)

s3 = s1 + s2

print(s3.m1)
print(s3.m2)

print("-----")

class Student:

    def __init__(self, m1, m2):

        self.m1 = m1

        self.m2 = m2

    def __gt__(self, other):

        r1 = self.m1 + self.m2

        r2 = other.m1 + other.m2

        if r1 > r2:

            return True

        else:

            return False



s1 = Student(60, 90)
s2 = Student(50, 96)

if s1 > s2:

    print("S1 Win")

else:

    print("S2 Win")


print("----")

a = 10

print(a)
print(a.__str__())

class Student:

    def __init__(self, m1, m2):

        self.m1 = m1

        self.m2 = m2

    def __str__(self):

        return self.m1, self.m2


s1 = Student(20, 80)
s2 = Student(10, 90)


print(s1.__str__())
print(s2.__str__())


print("---")

class Student:

    def __init__(self, m1, m2):

        self.m1 = m1

        self.m2 = m2

    def __str__(self):

        return "{} {}".format(self.m1, self.m2)


s1 = Student(20, 80)
s2 = Student(10, 90)


print(s1)
print(s2)