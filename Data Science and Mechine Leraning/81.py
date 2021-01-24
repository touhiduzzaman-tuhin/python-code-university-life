import pandas as pd

from numpy.random import randn

li = pd.DataFrame(randn(5, 4), index=['A', 'B', 'C', 'D', 'E'], columns=['W', 'X', 'Y', 'Z'])

print(li)

print("----")


li1 = li['W'] > 0

li2 = li[li1]

li3 = ['X', 'Z']

li4 = li2[li3]

print(li4)