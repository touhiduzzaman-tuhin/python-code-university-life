import re

p = r"[aeiou]"

if re.match(p, "ojdkjdkhh"):

    print("Match")

else:

    print("Not Match")