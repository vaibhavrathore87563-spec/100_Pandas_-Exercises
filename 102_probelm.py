# Reshape the dataframes USE-> melt fnxn
import pandas as pd
var = pd.DataFrame({"days":[1,2,3,4,5,6] , "eng":[10,14,15,16,17,10] , "math":[17,98,34,67,12,55]})

print(pd.melt(var))