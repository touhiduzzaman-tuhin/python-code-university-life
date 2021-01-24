import re

pattern = r"color"

text1 = "Red is the color, I love red color"

text2 = re.sub(pattern, "colour", text1)

print(text2)

text3 = re.sub(pattern, "colour", text1, count=1)

print(text3)