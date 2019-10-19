import pandas as pd
import json

data = pd.read_csv("AirQualitySystem.csv")
data = data.dropna(axis="columns")

col_list = ["Latitude", "Longitude",
            "Parameter Name", "Date GMT", 
            "Time GMT", "Sample Measurement", 
            "Unit of Measure", "State Name", 
            "County Name"]
df = data[col_list]
print(df.head())
print('test')
