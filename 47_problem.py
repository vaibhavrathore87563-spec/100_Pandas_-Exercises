# Read csv and check how much index in csv file
import pandas as pd
read_student_csv = pd.read_csv("students.csv")
print(read_student_csv)
print(read_student_csv.index)

#output=RangeIndex(start=0, stop=9, step=1)
