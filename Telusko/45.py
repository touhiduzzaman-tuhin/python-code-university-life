def div(a, b):

    return a / b

v = div(2, 4)

print(v)

print("---")

def div(a, b):

    if a < b:

        a, b = b, a

    return a / b

v = div(2, 4)

print(v)

print("-----")

def div(a, b):

    return a / b


def smart_div(func):

    def change(a, b):

        if a < b:

            a, b = b, a

        return func(a, b)

    return change 


div1 = smart_div(div)

v = div1(2, 4)

print(v)