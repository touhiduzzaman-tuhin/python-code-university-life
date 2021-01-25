import re

pattern = r"color"

if re.search(pattern, "Red is a color, I Love red color"):

    print("Found")

else:

    print("Not Found")