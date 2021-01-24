import re

p = r"(ab)+"

if re.match(p, "ababjkdskdjab"):

    print("Match")

else:

    print("Not Match")