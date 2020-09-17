#!/usr/bin/env python3
 
import pandas as pd
import numpy as np
 
def special_missing_values():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    m = (df["LW"] == "New") | (df["LW"] == "Re")
    df.loc[m, "LW"] = np.nan
    df["LW"] = pd.to_numeric(df["LW"])
    m2 = df["LW"] < df["Pos"]
    return df[m2]
 
def main():
    df = special_missing_values()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes, sep="\n")
    print(df)
 
if __name__ == "__main__":
    main()
 

