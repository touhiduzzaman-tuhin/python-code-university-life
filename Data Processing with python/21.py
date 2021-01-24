import pandas

import os

os.chdir("F:\CODE\Python\Data processing with python")

df1 = pandas.read_csv("data.csv", index_col=0)

print(df1['Temp'])

print("---")

n = df1['Temp'].mean()

print(n)

print("---")

print(df1.loc['Day 1'])