# Replace multiple values with one value 

import pandas as pd
var = pd.read_csv("students.csv")
var1 = var.replace([20,0,25,21],254)
print(var1)