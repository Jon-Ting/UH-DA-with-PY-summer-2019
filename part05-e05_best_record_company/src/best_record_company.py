#!/usr/bin/env python3

import pandas as pd

def best_record_company():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    df = df.groupby("Publisher") 
    woc_sum = df["WoC"].sum().sort_values()
    print(woc_sum)
    print(df)
    best_df = df.get_group(woc_sum.index[-1])
    print(best_df)
    return best_df

def main():
    best_record_company()    
    

if __name__ == "__main__":
    main()
