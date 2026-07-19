# if you want to fetch some data in csv file Use--> describe() fnxn this fnxn give the data like : (count, mean, std, min, 25%, 50%, 75%, max)
import pandas as pd
fetch_data = pd.read_csv("students.csv")
print(fetch_data.describe())

'''   output          Age      Marks
count   9.000000   9.000000
mean   20.777778  71.333333
std     1.201850  29.398129
min    19.000000   0.000000
25%    20.000000  67.000000
50%    21.000000  81.000000
75%    21.000000  87.000000
max    23.000000  95.000000'''