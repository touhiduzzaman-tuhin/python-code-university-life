import re

p = r"(ab)*"

if re.match(p, "colutrur"):

    print("Match")

else:

    print("Not Match")