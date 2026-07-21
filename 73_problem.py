# Fill the Nan value with limit -> limit works based on columns
import pandas as pd
var = pd.read_csv("students.csv")
var1 = var.fillna("limit",limit=1)
print(var1)