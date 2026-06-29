import pandas as pd
import os
data_folder = "data/raw"
files = os.listdir(data_folder)
print(files)
for file in files:

    if file.endswith(".csv"):

        path = os.path.join(data_folder, file)

        df = pd.read_csv(path)

        print("="*60)
        print(file)
        print("="*60)

        print("Shape")
        print(df.shape)

        print("\nData Types")
        print(df.dtypes)

        print("\nFirst Five Rows")
        print(df.head())
        print (df.isnull().sum())
