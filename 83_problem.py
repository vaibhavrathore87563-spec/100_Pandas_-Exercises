# How to merge two Dataframes use->how=left

import pandas as pd

var1 = pd.DataFrame({"A":[1,2,3,4,5],"B":[11,12,13,14,15]})

var2 = pd.DataFrame({"A":[7,8,5,4,2],"C":[22,18,32,14,54]})

print(pd.merge(var1,var2,how="left"))