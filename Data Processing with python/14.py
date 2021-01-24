import pandas

import os

os.chdir("F:\CODE\Python\Data processing with python")

df1 = pandas.read_csv("coma.txt")

n = df1.head()

df2 = df1.to_csv("colon.txt", sep=':')

print(n)

print(df2)