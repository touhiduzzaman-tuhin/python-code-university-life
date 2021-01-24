import numpy as np

import pandas as pd

li = pd.Series(data=[1, 2, 3, 4], index=['Ban', 'Ind', 'Pak', 'Aus'])

li1 = pd.Series(data=[1, 2, 5, 4], index=['Ban', 'Ind', 'Sri', 'Aus'])

li2 = li + li1

print(li2)