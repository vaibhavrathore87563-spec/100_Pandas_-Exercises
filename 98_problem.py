import pandas as pd
var = pd.DataFrame({
      "Name": ["Riya","Sourabh","Divyansh","OM","vaibhav"],
     "Marks": [70,88,90,92,88]
})
var1 = var.groupby("Marks")


for x, y in var1:
    print("Group:", x)
    print(y)
    print( )
    print(var1.min()) 
    print(var1.max())