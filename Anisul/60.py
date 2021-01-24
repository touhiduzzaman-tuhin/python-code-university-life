class Student:

    roll = ""
    gpa = ""


tuhin = Student()

print(isinstance(tuhin, Student))

print("\n")

tuhin.roll = 101
tuhin.gpa = 3.86

print(f"Roll : {tuhin.roll}, Gpa : {tuhin.gpa}")


print("\n")

Shahed = Student()

Shahed.roll = 102
Shahed.gpa = 2.86

print(f"Roll : {Shahed.roll}, Gpa : {Shahed.gpa}")

