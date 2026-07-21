#Replace using dictionart

import pandas as pd
var = pd.read_csv("students.csv")
print(var)
print(var.replace({"City": '[A-Z]'} , 22 , regex=True))