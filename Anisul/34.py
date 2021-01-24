letter = 0
word = 0
digit = 0

x = input("Enetr A List : ")

for i in x:

    i = i.lower()

    if i >= 'a' and i <= 'z':

        letter += 1

    elif i >= '0' and i <= '9':

        digit += 1

    elif i == ' ':

        word += 1


print("Number of Letter : ", letter)
print("Number of Word : ", word+1)
print("Number of Digit : ", digit)