# Linear Search

li = []

n = int(input("Enter How many Number : "))

print("Enter the elements : ")

for i in range(n):

    e = int(input())

    li.append(e)

print(li)

print("---")

a = int(input("Enter The Search Element : "))

def linear_search(li, n, a):

    for i in range(n):

        if li[i] == a:
            
            return 1, i

    return -1




v, k = linear_search(li, n, a)

if v == 1:

    print("Found At : ", k+1)

else:

    print("Not Found")