#!/usr/bin/env python3

import pandas as pd

def top_bands():
    uktop = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    bands = pd.read_csv("src/bands.tsv", sep="\t")
    # print(uktop)
    # print(bands)
    bands["Band"] = bands["Band"].str.upper()
    df = pd.merge(uktop, bands, how="inner", left_on=["Artist"], right_on=["Band"])
    print(df)
    return df

def main():
    top_bands()

if __name__ == "__main__":
    main()
