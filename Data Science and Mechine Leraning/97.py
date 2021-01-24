import numpy as np

import pandas as pd

li = {'A': [1, 2, np.nan], 'B': [1, np.nan, np.nan], 'C': [1, 2, 3]}

li2 = pd.DataFrame(li)

li3 = li2.dropna(axis=1)

print(li3)