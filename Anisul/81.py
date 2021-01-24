import re

pattern = r"color"

if re.match(pattern, "Red is the color, I love red color"):

    print("Match")


else:

    print("Not Match")