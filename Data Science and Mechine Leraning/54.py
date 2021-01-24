import numpy as np

import pandas as pd

li = ['a', 'b', 'c']

li1 = [10, 11, 12]

li3 = pd.array(li1)

li2 = pd.Series(data=li3, index=li)

print(li2)