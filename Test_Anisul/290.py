import re

p = r"a{1,3}$"

if re.match(p, "aaa"):

    print("Match")

else:

    print("Not Match")