list = [1, 2, 3, 4, 5]

n = 5


def Search(list, n):

    for i in list:

        if i == n:

            return True

    return False

if Search(list, n):

    print("Found")

else:

    print("Not Found")