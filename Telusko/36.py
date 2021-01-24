def Student(name, *data):

    print(name)
    print(data)

Student('Tuhin', 25, 'Rangpur', 1719206623)

print("----")

def Student(name, **data):

    print(name)
    print(data)

Student('Tuhin', age = 25, city = 'Rangpur', phone = 1719206623)

print("----")

def Student(name, **data):

    print(name)


    for i, j in data.items():

        print(i, j)

Student('Tuhin', age = 25, city = 'Rangpur', phone = 1719206623)

print("----")