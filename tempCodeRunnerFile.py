import pandas as pd
var = pd.read_csv("Test.csv")
print(var.dropna(how="any"))