import re

p = r"color"

text = "Do you know what wcolor is not bad"

m = re.search(p, text)

if m:

    print(m.start())

    print(m.end())


    print(m.span())