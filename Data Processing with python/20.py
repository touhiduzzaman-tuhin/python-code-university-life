import pandas

import os

os.chdir("F:\CODE\Python\Data processing with python")

df1 = pandas.read_csv("colon.csv", index_col=0)

print(df1)

