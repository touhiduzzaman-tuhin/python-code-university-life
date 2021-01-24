class Student:

    roll = ""
    gpa = ""

    def set_value(self, roll, gpa):

        self.roll = roll

        self.gpa = gpa

    def display(self):

        print(f"Roll : {self.roll}, Gpa : {self.gpa}")


tuhin = Student()
tuhin.set_value(101, 3.87)
tuhin.display()

shahed = Student()
shahed.set_value(102, 2.87)
shahed.display()