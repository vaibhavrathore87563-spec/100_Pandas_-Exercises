#avg(),highest(),maximum(),minimum(),sum(),count()
import pandas as pd

marks = pd.Series([35,48,56,72,81,90,99,66,100,54])

print("Total marks:", marks.sum())
print("Average marks:", marks.mean())
print("Highest marks:", marks.max())
print("Lowest marks:", marks.min())
print("Total Students:", marks.count())