class Stdent:

    roll = ""
    gpa = ""

    def __init__(self, roll, gpa):

        self.roll = roll

        self.gpa = gpa

    def display(self):

        print(f"Roll : {self.roll}, Gpa : {self.gpa}")


tuhin = Stdent(101, 3.87)
tuhin.display()

shahed = Stdent(102, 2.87)
shahed.display()