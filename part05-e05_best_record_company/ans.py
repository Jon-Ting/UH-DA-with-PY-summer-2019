#!/usr/bin/env python3
 
import pandas as pd
 
def best_record_company():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    df2 = df.groupby("Publisher").sum()
    best_company = df2["WoC"].idxmax()
    return df[df["Publisher"] == best_company]
 
def main():
    df = best_record_company()
    print("Shape:", df.shape)
    print("Column names:", df.columns)
    print("dtypes:", df.dtypes)
    print(df)
    
 
if __name__ == "__main__":
    main()
 
