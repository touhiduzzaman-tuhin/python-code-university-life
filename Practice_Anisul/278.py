import re

pattern = r"color"

print(re.match(pattern, "color : Red is a color, I Love red color"))

print(re.match(pattern, "Red is a color, I Love red color"))

print(re.search(pattern, "Red is a color, I Love red color"))
