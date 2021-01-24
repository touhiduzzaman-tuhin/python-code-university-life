import re

pattern = r"color"

text = "My favourit ecolor is red"

match = re.search(pattern, text)

if match:

    print(match.start())
    print(match.end())
    print(match.span())