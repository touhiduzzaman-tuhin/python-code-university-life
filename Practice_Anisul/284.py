import re

p = r"^col...ur$"

if re.match(p, "colutrur"):

    print("Match")

else:

    print("Not Match")