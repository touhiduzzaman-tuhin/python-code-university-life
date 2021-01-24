import pandas as pd

from numpy.random import randn

li = pd.DataFrame(randn(5, 4), index=['A', 'B', 'C', 'D', 'E'], columns=['W', 'X', 'Y', 'Z'])

print(li)

print("----")

li['New'] = li['X'] + li['Z']

print("----")

print(li)