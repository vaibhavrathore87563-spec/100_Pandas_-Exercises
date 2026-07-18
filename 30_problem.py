# Delete column using pop() question-2
import pandas as pd
var = pd.DataFrame({"A":[2,3,4,5,6] , "B":[7,8,9,0,1] , "c":[6,5,4,3,2]})
print(var)
var.pop("c")
print(var)