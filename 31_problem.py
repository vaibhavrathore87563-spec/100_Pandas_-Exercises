# Delete column using del
import pandas as pd
var = pd.DataFrame({"A":[3,4,8,9,6] ,"B":[4,7,9,0,2] ,"C":[4,8,6,4,7]})
print(var)
del var["B"]
print(var)
