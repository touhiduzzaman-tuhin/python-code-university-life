student = {

    'name' : 'tuhin',
    'id' : '162-15-7727',
    'home-town' : ['rangpur', 'dhaka'],
    'age' : 25
}

print(student)

print(type(student))

print(student.values())

print(student.keys())

print(student.items())

for i in student:

    print(i, student[i])

print("---")

for i, j in student.items():

    print(i, j)


print("--")

for i in student.keys():

    print(i)

print("--")

for i in student.values():

    print(i)

print("---")


print(student["name"])

student['name'] = 'kona'

print(student)

del student['age']

print(student)

print(student.get('name'))

print(student.get('dob'))

print(student.get('dob', 'value Not Declare'))

h = student.pop('home-town')

print(h)

print(student)

student['hobby'] = 'playing'

print(student)

print(len(student))

print(student.__len__())