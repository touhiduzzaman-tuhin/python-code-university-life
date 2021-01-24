import re

pattern = r"a{1,3}$"

if re.match(pattern, "aa"):

    print("Match")
