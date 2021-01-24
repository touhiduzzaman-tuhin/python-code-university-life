import numpy as np

import pandas as pd

li = pd.Series(data=[1, 2, 3, 4], index=['Ban', 'Ind', 'Pak', 'Aus'])

print(li)

print("---")

li1 = pd.Series(data=[1, 2, 5, 4], index=['Ban', 'Ind', 'Sri', 'Aus'])

print(li1)

print("---")

print(li['Ban'])