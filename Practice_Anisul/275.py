import re

pattern = r"color"

if re.match(pattern, "color : Red is a color, I Love red color"):

    print("Match")

else:

    print("Not Match")