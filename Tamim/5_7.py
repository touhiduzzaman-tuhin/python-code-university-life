class Rectangle:

    def __init__(self):
        print("Inside init Of Rectangle")

    def area(self, x, y):
        return self.x * self.y


class Square(Rectangle):
    pass

r = Rectangle()

sq = Square()

print(r)
print(sq)

class Rectangle:

    def __init__(self):
        print("Inside init Of Rectangle")

    def area(self, x, y):
        return x * y


class Square(Rectangle):

    def __init__(self):
        print("Inside init Of Square")


    def area(self, x):
        return x * x


r = Rectangle()

sq = Square()

area = sq.area(5, 5)

ar = sq.area(5)



print(r)
print(sq)
print(area)
print(ar)


print("\n")
print("\n")


class Rectangle:

    def __init__(self):
        print("Inside init Of Rectangle")

    def area(self, x, y):
        return x * y


class Square(Rectangle):

    def __init__(self):
        print("Inside init Of Square")


    def area(self, x):
        return Rectangle(self, x, x)


r = Rectangle()

sq = Square()

area = sq.area(5)


print(area)

