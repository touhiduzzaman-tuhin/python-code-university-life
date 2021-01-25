import re

p = r"ice(-)?creem"

if re.match(p, 'ice-creem'):

    print("match")

else:

    print("Not Match")