li = [11, 22, 33, 44, 55, 66, 77, 88, 99]

for i in range(len(li)):

    if li[i] % 5 == 0:

        print(li[i], "Found At Position :",i+1)

        break

print("End")