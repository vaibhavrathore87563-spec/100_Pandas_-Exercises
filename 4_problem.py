#Create a Dataframe(city,population State)
import pandas as pd

data = {
    "City": ["Indore","Ujjain","Bhopal"],
    "Population": [11000,8000,7000],
    "State": ["Mp","Mp","Mp"]
}

df = pd.DataFrame(data)
print(df)