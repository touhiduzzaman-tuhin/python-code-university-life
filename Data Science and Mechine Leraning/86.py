import pandas as pd

from numpy.random import randn

li = pd.DataFrame(randn(5, 4), index=['A', 'B', 'C', 'D', 'E'], columns=['W', 'X', 'Y', 'Z'])

print(li)

print("----")

val = 'My Na Ja Ka Ha'.split()

li['States'] = val


li2 = li.set_index('States')

print(li2)