# Fill the Nan value with the Forward value use axis=

import pandas as pd
var = pd.read_csv("students.csv")
print(var.ffill(axis=1))