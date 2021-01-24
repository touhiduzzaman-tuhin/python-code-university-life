def add(x, y):

    sum = x + y

    return sum

v = add(10, 20)

print(v)

print(add(100, 20))

def large(x, y):

    if x > y:

        return x

    else:

        return y

    
v = large(10, 20)

print(v)

print(large(20, 31))

max = large

print(max(10, 21))