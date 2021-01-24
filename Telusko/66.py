
def Search(list, n):

    c = 0

    i = 0

    while i < len(list):

        if list[i] == n:

            globals()['c'] = i

            return True

        i += 1

    return False


list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

n = 6

if Search(list, n):

    print("Found at : ", c)

else:

    print("Not Found")
