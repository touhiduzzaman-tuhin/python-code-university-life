import re

pattern = r"^col.our$"

if re.match(pattern, "colyour"):

    print("Match")