import pandas

import os

os.chdir("F:\CODE\Python\Data processing with python")

df1 = pandas.read_csv("data.csv", index_col=0)


df = df1.loc['Day 3': 'Day 5', 'Hour' : 'Pre']

print(df)