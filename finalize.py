import os
import pandas as pd
from tqdm import tqdm


def compress_data(data_path, year):
    df = pd.read_csv(data_path)
    df = df.drop("Unnamed: 0", axis=1)
    df["Year"] = year
    return df


def concat(dataframes):
    maindf = dataframes[0]
    for i in range(1, len(dataframes)):
        df = dataframes[i]
        maindf = pd.concat([maindf, df], axis=0)
    return maindf


if os.path.isdir("./finalized_data") != True:
    os.mkdir("./finalized_data")
    print("Creating directory")
else:
    print("Already exists")

extract_to = "./finalized_data"
df_toxins = {"Ozone": [],
             "SO2": [],
             "CO": [],
             "NO2": []}
# compress data
for dirpath, dirnames, filenames in os.walk("formatted/"):
    for f in filenames:
        data_path = dirpath + "/" + f
        year = f[12:16]
        if year >= 2009:
            if "NO2" in dirpath:
                klist = df_toxins["NO2"]
                klist.append(compress_data(data_path, year))
                df_toxins["NO2"] = klist
            elif "CO" in dirpath:
                klist = df_toxins["CO"]
                klist.append(compress_data(data_path, year))
                df_toxins["CO"] = klist
            elif "SO2" in dirpath:
                klist = df_toxins["SO2"]
                klist.append(compress_data(data_path, year))
                df_toxins["SO2"] = klist
            elif "Ozone" in dirpath:
                klist = df_toxins["Ozone"]
                klist.append(compress_data(data_path, year))
                df_toxins["Ozone"] = klist
            
for toxin, dataframes in tqdm(df_toxins.items()):
    df = concat(dataframes)
    df.columns[0] = "ID"
    for index, row in df.iterrows():
        row["ID"] = index + 1
    df.to_csv(extract_to+"/"+toxin+"_v2.csv")
