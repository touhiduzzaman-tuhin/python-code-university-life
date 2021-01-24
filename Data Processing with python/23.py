import pandas

import os

os.chdir("F:\CODE\Python\Data processing with python")

df1 = pandas.read_csv("data.csv", index_col=0)

print(df1.loc['Day 3', 'Hour'])

print("---")

print(df1.iloc[2, 3])

print(df1.loc['Day 3' : 'Day 6', 'Year' : 'Temp'])

df = df1.loc['Day 3: Day 5', 'Hour' : 'Pre']

print(df)