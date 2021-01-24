
def sort(li):

    for i in range(len(li)):

        for j in range(i):

            if li[j] > li[j+1]:

                temp = li[j]

                li[j] = li[j+1]

                li[j+1] = temp

li = [1, 5, 9, 2, 3, 6, 8, 4, 7]

sort(li)

print(li)
