def student(x, y, z, a, b):

    print(x, y, z, a, b)

student(1, 2, 3, 4, 5)

def Student(*details):

    print(details)

    print(details[0])
    print(details[1])
    print(details[2])
    print(details[2:])
    print(details[-1])

Student(1, 2, 3, 4, 5, 6, 7, 8)


def add(*number):

    sum = 0

    for i in number:

        sum += i


    print(sum)

add(10, 20)
add(10, 20, 30)
add(10, 20, 30, 40, )
add(10, 20, 30, 40, 50)


def Student(**details):

    print(details)
    print(details["id"])
    print(details["name"])


Student(id = 101, name = "Tuhin")
Student(id = 102, name = "Kona")