#!/usr/bin/env python3

import pandas as pd
import numpy as np

def special_missing_values():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    df = df.replace({"New": None, "Re": None})
    # print(df.isnull())
    df = df.dropna(how="any")
    # print(df)
    df = df[df["Pos"].astype(int) > df["LW"].astype(int)]
    return df

def main():
    print(special_missing_values())

if __name__ == "__main__":
    main()
