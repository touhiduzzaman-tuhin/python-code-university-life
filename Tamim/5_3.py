class Square:

    side = 0

    def area(self):
        return self.side * self.side

sqr1 = Square()
area = sqr1.area()
print(area)

print("\n")

sqr1 = Square()
sqr1.side = 5
area = sqr1.area()
print(area)



class Circle:

    def area(self):
        return self.side * self.side

crl1 = Circle()
crl1.side = 10
area = crl1.area()
print(area)