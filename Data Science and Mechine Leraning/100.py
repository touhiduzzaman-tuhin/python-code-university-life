import numpy as np

import pandas as pd

li = {'A': [1, 2, np.nan], 'B': [1, np.nan, np.nan], 'C': [1, 2, 3]}

li2 = pd.DataFrame(li)

print(li2['A'])

print("----")

li3 = li2['A'].fillna(value=li2['A'].mean())

print(li3)