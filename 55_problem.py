#convert csv to Numpy array using numpy

import numpy as np
import pandas as pd
pandas_array = pd.read_csv("students1.csv")
arr = np.asarray(pandas_array)
print(arr)