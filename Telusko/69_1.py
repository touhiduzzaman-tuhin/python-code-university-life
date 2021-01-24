def sort(li):

    for i in range(len(li)):

        minpos = i

        for j in range(i, len(li)):

            if li[j] < li[minpos]:

                minpos = j


        temp = li[i]

        li[i] = li[minpos]

        li[minpos] = temp

        print(li)

li = [1, 5, 9, 2, 3, 6, 8, 4, 7]

sort(li)

print(li)
