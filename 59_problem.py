#fetch particular value use-> iloc[]
import pandas as pd
var = pd .read_csv("students1.csv")
print(var.iloc[0,4])