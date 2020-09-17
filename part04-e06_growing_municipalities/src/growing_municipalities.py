#!/usr/bin/env python3

import pandas as pd

def growing_municipalities(df):
    increase_df = df[df["Population change from the previous year, %"] > 0]
    proportion = increase_df.shape[0] / df.shape[0]
    print("Proportion of growing municipalities: {0:.1f}%".format(proportion))
    return proportion
    
def main():
    df = pd.read_csv("src/municipal.tsv", sep="\t", index_col=0)
    df = df["Akaa": "Äänekoski"]
    growing_municipalities(df)

if __name__ == "__main__":
    main()
