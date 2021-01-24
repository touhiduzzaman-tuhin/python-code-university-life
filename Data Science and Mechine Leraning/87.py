import numpy as np

import pandas as pd

out = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']

inside = [1, 2, 3, 1, 2, 3]

li = list(zip(out, inside))

print(li)

print("----")

li1 = pd.MultiIndex.from_tuples(li)

print(li1)