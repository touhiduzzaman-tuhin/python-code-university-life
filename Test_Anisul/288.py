import re

p = r"a*b"

if re.match(p, "bacbjkdskdjacb"):

    print("Match")

else:

    print("Not Match")