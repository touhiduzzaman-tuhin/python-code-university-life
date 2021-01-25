def voter(n):

    if n < 18:

        raise ValueError("Value Error Found")

    return "You Are Allow to Vote"


try:

    print(voter(19))

except ValueError as v:

    print(v)