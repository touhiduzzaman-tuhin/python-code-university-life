# Linear search

li = [1, 2, 3, 4, 5]

n = 3

p = 0

def linear_search(list, n):

    for i in range(len(li)):

        if li[i] == n:

            globals()['p'] = i

            return True

    return False

if linear_search(li, n):

    print("Found At :", p+1)

else:

    print("Not Found")