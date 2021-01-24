def Student(name, age):

    print("Name : ", name)

    print("Age : ", age)

Student('Tuhin', 25)

print("----")


def Student(name, age):
    print("Name : ", name)

    print("Age : ", age)


Student(25, 'Tuhin')

print("----")

def Student(name, age):
    print("Name : ", name)

    print("Age : ", age)


Student(age = 25, name='Tuhin')

print("----")


def Student(name, age = 18):
    print("Name : ", name)

    print("Age : ", age)


Student('Tuhin')

print("----")

def Student(name, age = 18):
    print("Name : ", name)

    print("Age : ", age)


Student('Tuhin', 25)

print("----")



def add(x, *y):

    print(x)
    print(y)


add(1, 2, 3 , 5)

print("----")


def add(*y):

    print(y)


add(1, 2, 3, 5)

print("----")


def add(*y):

    sum = 0

    for i in y:

        sum = sum + i

    print(sum)


add(1, 2, 3, 5)

print("----")
