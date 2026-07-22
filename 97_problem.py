# Get perticular data using get_group("")
import pandas as pd

var = pd.DataFrame({
     "Name": ["Riya","Sourabh","Divyansh","OM","vaibhav"],
     "Marks": [70,88,90,92,88]
})

var1 = var.groupby("Marks")

for x , y in var1:
    print("Group:" , x)
    print(y)
    print( )

    # Get only the group where Marks = 80
print(var1.get_group(88))