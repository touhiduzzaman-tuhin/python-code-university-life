class Square:

    def area(self):

        return self.side * self.side


s = Square()

n = int(input("Enter The Side value : "))

s.side = n

area = s.area()

print("Area : ", area)