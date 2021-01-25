w = 0
d = 0
v = 0
l = 0

x = input("Enter A String : ")

for i in x:

    x = x.lower()

    if i >= '0' and i <= '9':

        d += 1

    elif i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':

        v += 1

    elif i >= 'a' and i <= 'z':

        l += 1

    elif i == ' ':

        w += 1


print("Word : ", w+1)

print("Digit : ", d)

print("Vowel : ", v)

print("Letter : ", l)
