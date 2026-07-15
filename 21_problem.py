#Arithmatic operation (-)
import pandas as pd
S = pd.DataFrame({"A":[1,2,3,4,5] , "B":[9,8,7,6,5]})
print(S)
S["C"] = S["A"] -S ["B"]
print(S)