list = [1, 2, 3, 4, 5]

n = 3

c = 0

def Search(list, n):

    for i in range(len(list)):

        if list[i] == n:

            globals()['c'] = i

            return True

    return False

if Search(list, n):

    print("Found at : ", c+1)

else:

    print("Not Found")