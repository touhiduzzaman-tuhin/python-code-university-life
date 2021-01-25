import re

p = r"a+b"

if re.match(p, "abacbjkdskdjacb"):

    print("Match")

else:

    print("Not Match")