class Square:

    def __init__(self):

        self.side = 5
        
    def area(self):

        return self.side * self.side

s = Square()

area = s.area()

print("Area = ", area)