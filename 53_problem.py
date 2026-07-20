import pandas as pd
fetch_last_rows = pd.read_csv("students1.csv")
print(fetch_last_rows.index.array)