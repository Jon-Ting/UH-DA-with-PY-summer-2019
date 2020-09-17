#!/usr/bin/env python3
 
import pandas as pd
 
def swedish_and_foreigners():
    df = pd.read_csv("src/municipal.tsv", index_col=0, sep="\t")
    df = df["Akaa":"Äänekoski"]
    m = ((df["Share of Swedish-speakers of the population, %"] > 5.0) &
         (df["Share of foreign citizens of the population, %"] > 5.0))
    df = df[m]
    df = df[["Population", "Share of Swedish-speakers of the population, %",
             "Share of foreign citizens of the population, %"]]
    return df
 
def main():
    df = swedish_and_foreigners()
    print("Shape: {}, {}".format(*df.shape))
    print(df)
    for i in range(3):
        print(df.iloc[i,i])
 
if __name__ == "__main__":
    main()
 
