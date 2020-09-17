#!/usr/bin/env python3

import pandas as pd
import numpy as np


empty_row = pd.Series([np.nan] * 7, index=["Pos", "LW", "Title", "Artist", "Publisher", "Peak Pos", "WoC"])


def last_week():
    # Read data, replace entries, remove missing ranks
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    # print(df)
    df2 = df.replace({"New": np.nan, "Re": np.nan})
    df2 = df2[df2["Pos"].notnull() & df2["LW"].notnull()]
    df2["LW"] = df2["LW"].astype(int)
    # print(df2)

    # Identify the missing ranks
    missing_rank = list(np.arange(1, 41))
    for i in df2["LW"]:
        if i in range(1, 41):
            missing_rank.remove(i)
    # print(missing_rank)
    
    # Make up the rows to 40
    for i in range(df.shape[0] - df2.shape[0]):
        df2 = df2.append(empty_row, ignore_index=True)
    # print(df2)
   
    # Add in the missing ranks and sort the DataFrame
    fill = pd.DataFrame(index=df2.index[df2.isnull().any(axis=1)], data=missing_rank, columns=["LW"])
    # print(fill)
    df2 = df2.fillna(fill)
    df2 = df2.sort_values("LW")
    # print(df2)    

    # Adjust column entries
    wrong_peak1 = df2.where(df2["Peak Pos"] != df2["Pos"], np.nan)
    print(wrong_peak1["Peak Pos"])
    wrong_peak2 = df2.where(df2["Peak Pos"] >= df2["LW"], np.nan)
    print(wrong_peak2["Peak Pos"])
    wrong_peak1["Peak Pos"] = wrong_peak1["Peak Pos"].astype(float)
    wrong_peak2["Peak Pos"] = wrong_peak2["Peak Pos"].astype(float)
    wrong_peak = df2[wrong_peak1["Peak Pos"].notnull() | wrong_peak2["Peak Pos"].notnull()]
    print(wrong_peak)
    # filter_df = df2["Peak Pos"] < df2["Pos"] & df2["Pos"] == df2["LW"]
    # print(df2)
    df2["Peak Pos"] = wrong_peak["Peak Pos"]
    df2["Pos"] = df2["LW"]
    df2["LW"] = np.nan
    df2["WoC"] = df2["WoC"] - 1
   
    return df2


def main():
    df = last_week()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes)
    print(df)


if __name__ == "__main__":
    main()
