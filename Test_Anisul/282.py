import re

p =r"color"

text = 'Red is the color and i love the color and color'

text1 = re.sub(p, "Colour", text, count=2)

print(text)
print(text1)