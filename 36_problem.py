#Read file and access particular Row
import pandas as pd
read_students_csv = pd.read_csv("students.csv",nrows=5)
print(read_students_csv)