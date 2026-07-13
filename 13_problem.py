# series method of pandas ,sum(),minimum value(),maximum value(),mean(), median(), standard deviation(), count(),var()
import pandas as pd

marks = pd.Series([10,20,30,40,50])

print("sum:",marks.sum())
print("Minimum value:",marks.min())
print("Maximum value:",marks.max())
print("mean:",marks.mean())
print("Median:",marks.median())
print("count", marks.count())
print("Standard Deviation:", marks.std())
print("Variance:", marks.var())