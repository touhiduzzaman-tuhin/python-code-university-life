import re

pattern = r"color"

if re.match(pattern, "Red is a color, I Love red color"):

    print("Match")

else:

    print("Not Match")