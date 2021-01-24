import re

pattern = r"ice(-)?creem*"

if re.match(pattern, "icecreem"):

    print("Match")
