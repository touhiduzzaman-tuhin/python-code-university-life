import pandas

import os

os.chdir("F:\CODE\Python\Data processing with python")

df1 = pandas.read_csv("coma.txt")


df2 = df1.to_csv("test.csv", header=None, index= None)

