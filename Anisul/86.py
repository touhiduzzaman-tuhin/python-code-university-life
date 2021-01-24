import re

pattern = r"colo..r"

if re.match(pattern, "colouyr"):

    print("Match")