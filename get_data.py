import pandas as pd
import os

def get_data(data_path, extract_to):
    df = pd.read_csv(data_path)
    df = df.dropna(axis="columns")
    colnames = ["Latitude", "Longitude",
                "Date Local", "Units of Measure",
                "Arithmetic Mean", "1st Max Value",
                "1st Max Hour", "State Name",
                "City Name"]
    df = df[colnames]

    city_names = ["Prattvile", "San Francisco",
                  "Chicago", "New York", "Memphis"]
    df = df.loc[df["City Name"].isin(city_names)]
    df.to_csv(extract_to)


if os.path.isdir("./formatted") != True:
    os.mkdir("./formatted")
    print("Creating directory")
else:
    print("Already exists")

mdirs = ["formatted/NO2",
         "formatted/CO",
         "formatted/SO2",
         "formatted/Ozone"]
# make dirs
for mdir in mdirs:
    if os.path.isdir(mdir) != True:
        os.mkdir(mdir)
        print("Creating directory " + mdir)
    else:
        print(mdir + " already exists")

for dirpath, dirnames, filenames in os.walk("data/"):
    for f in filenames:
        data_path = dirpath + "/" + f
        if "NO2" in dirpath:
            get_data(data_path, "formatted/NO2/" + f)
        elif "CO" in dirpath:
            get_data(data_path, "formatted/CO/" + f)
        elif "SO2" in dirpath:
            get_data(data_path, "formatted/SO2/" +f)
        elif "Ozone" in dirpath:
            get_data(data_path, "formatted/Ozone/" +f)
        print("Formatted " + data_path)

        

    
    
