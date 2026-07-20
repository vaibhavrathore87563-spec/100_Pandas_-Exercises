# Change data in your csv file

import pandas as pd
var = pd.read_csv("students1.csv")
var.loc[0 , "Name"] = "python"
print(var)