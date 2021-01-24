import re

pattern = r"color"

if re.search(pattern, "Red is the color, I love red color"):

    print("Match")


else:

    print("Not Match")