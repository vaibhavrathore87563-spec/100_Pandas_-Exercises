#Read csv file and fetch all coloumns name
import pandas as pd
fetch_csv = pd.read_csv("students.csv")
print(fetch_csv)
print(fetch_csv.columns)