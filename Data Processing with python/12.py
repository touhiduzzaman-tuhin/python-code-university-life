import pandas

import os

os.chdir("F:\CODE\Python\Data processing with python")

df1 = pandas.read_csv("space.txt")

n = df1.head()

print(n)