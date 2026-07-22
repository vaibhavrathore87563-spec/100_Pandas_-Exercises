#Join Two DataFrame With Index
import pandas as pd

var1 = pd.DataFrame({"A":[1,2,3,4,5] , "B":[11,12,13,14,15]})
var2 = pd.DataFrame({"C":[2,3] , "D":[4,5]})
print(var2.join(var1))
