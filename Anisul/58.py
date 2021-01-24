def voter(age):


    if age < 18:

        raise ValueError("Value Error Found")

    return "You Are allow to Vote"

try:
    print(voter(21))

except ValueError as e:
    print(e)