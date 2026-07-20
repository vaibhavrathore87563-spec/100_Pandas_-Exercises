#Get Particular Data

import pandas as pd
var = pd.read_csv("students.csv")
print(var.loc[[1,2,3,4], ["Name","Age"]])