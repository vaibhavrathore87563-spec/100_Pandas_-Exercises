# It is used to group rows that have the same value and then perform calculations on each group.
import pandas as pd
var = pd.DataFrame({
     "Name": ["Riya","Sourabh","Divyansh","OM","vaibhav"],
     "Marks":[100,90,80,70,70]
})
var1 = var.groupby("Marks")
for x,y in var1:
    print(x)
    print(y)
    print( )