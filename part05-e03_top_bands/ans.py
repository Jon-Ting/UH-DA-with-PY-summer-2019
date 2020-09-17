#!/usr/bin/env python3
 
import pandas as pd
 
def top_bands():
    top40 = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    bands = pd.read_csv("src/bands.tsv", sep="\t")
    bands["Band"] = bands["Band"].str.upper()
    result = pd.merge(top40, bands, left_on="Artist", right_on="Band")
    return result 
 
def main():
    df = top_bands()
    print("Shape:", df.shape)
    print("Columns:", df.columns)
    print(df)
 
if __name__ == "__main__":
    main()
 
