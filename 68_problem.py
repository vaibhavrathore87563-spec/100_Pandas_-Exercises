import pandas as pd
var = pd.read_csv("students.csv")
print(var)
print(var.fillna("python"))



#print(var.fillna("python"))
#DataFrame me jitni bhi NaN / missing values hain, unki jagah "python" likh do.