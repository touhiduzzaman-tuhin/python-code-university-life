from numpy.random import randn

import pandas as pd

out = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']

inside = [1, 2, 3, 1, 2, 3]

li = list(zip(out, inside))

li1 = pd.MultiIndex.from_tuples(li)

li2 = pd.DataFrame(randn(6, 2), index=li1, columns=['A', 'B'])

print(li2)