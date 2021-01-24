import pandas as pd

from numpy.random import randn

li = pd.DataFrame(randn(5, 4), index=['A', 'B', 'C', 'D', 'E'], columns=['W', 'X', 'Y', 'Z'])

print(li)

print("----")

li1 = li.loc['A', 'Z']

print(li1)

print("---")

li2 = li.loc[['A', 'C'], ['W', 'Z']]

print(li2)