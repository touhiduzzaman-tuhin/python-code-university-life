import numpy as np

import pandas as pd

li = {'A': [1, 2, np.nan], 'B': [1, np.nan, np.nan], 'C': [1, 2, 3]}

li2 = pd.DataFrame(li)

li2.dropna(inplace=True)

print(li2)