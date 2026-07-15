#Square root
import pandas as pd
marks = pd.DataFrame({ "Marks":
[10,20,30,40,50]})

marks["Square"] = marks["Marks"] **2
print(marks)