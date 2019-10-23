import matplotlib.pyplot as plt
import pandas as pd
import os

df_toxins = {"Ozone": None,
             "SO2": None,
             "CO": None,
             "NO2": None}

for dirpath, dirnames, filenames in os.walk("finalized_data/"):
    for f in filenames:
        data_path = dirpath + f
        data = pd.read_csv(data_path)
        threedee = plt.figure().gca(projection='3d')
        plot.scatter(data["Latitude"], df["Longitude"], df["Arithmetic Mean"])
        threedee.set_xlabel('Latitude')
        threedee.set_ylabel('Longitude-L')
        threedee.set_zlabel('Arithmetic Mean')
        plt.show()