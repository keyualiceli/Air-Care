import zipfile
import os
from tqdm import tqdm


def main():
    # new directories to create
    mdirs = ["data/NO2",
             "data/CO",
             "data/SO2",
             "data/Ozone"]
    # make dirs
    for mdir in mdirs:
        # dir already exist
        if os.path.isdir(mdir) != True:
            os.mkdir(mdir)
            print("Creating directory " + mdir)
        else:
            print(mdir + " already exists")

    # files to unzip by category
    files = {"Ozone": [],
             "SO2": [],
             "CO": [],
             "NO2": []}
    # Ozone (44201)	SO2 (42401)	CO (42101)	NO2 (42602)
    for (dirpath, dirnames, filenames) in os.walk("data/"):
        for f in filenames:
            if f.endswith(".zip"):
                if "44201" in f:
                    klist = files["Ozone"]
                    klist.append(os.path.join(dirpath, f))
                    files["Ozone"] = klist
                elif "42401" in f:
                    klist = files["SO2"]
                    klist.append(os.path.join(dirpath, f))
                    files["SO2"] = klist
                elif "42101" in f:
                    klist = files["CO"]
                    klist.append(os.path.join(dirpath, f))
                    files["CO"] = klist
                elif "42602" in f:
                    klist = files["NO2"]
                    klist.append(os.path.join(dirpath, f))
                    files["NO2"] = klist

    for category, zips in files.items():
        dir_extract = "data/" + category
        for fzip in tqdm(zips):
            with zipfile.ZipFile(fzip, 'r') as zip_ref:
                zip_ref.extractall(dir_extract)

if __name__ == '__main__':
    main()
