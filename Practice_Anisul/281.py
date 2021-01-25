import re

p = r"color"

text = "Red is the color and i love the color"

text1 = re.sub(p, "Colour", text)

print(text)
print(text1)