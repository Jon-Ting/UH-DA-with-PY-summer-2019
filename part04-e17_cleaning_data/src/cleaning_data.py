#!/usr/bin/env python3

import pandas as pd
import numpy as np


def cleaning_data():
    df = pd.read_csv("src/presidents.tsv", sep="\t")
    print(df)
    df["Vice-president"] = df["Vice-president"].str.split(" ")
    df["President"] = df["President"].str.split(" ")
    # print(df)
    for i in df["Vice-president"]:
        if "," in i[0] or "," in i[1]:
            # print(i)
            i.append(i[0].strip(","))
            del(i[0])
    for i in df["President"]:
        if "," in i[0] or "," in i[1]:
            i.append(i[0].strip(","))
            del(i[0])
    df["Vice-president"] = df["Vice-president"].str.join(" ")
    df["President"] = df["President"].str.join(" ")
    df["Vice-president"] = df["Vice-president"].str.title()
    df["President"] = df["President"].str.title()
    # print(df)
    df["Start"][0] = df["Start"][0].split(" ")[0]
    df["Last"] = df["Last"].replace("-", np.nan)
    df["Seasons"] = df["Seasons"].replace("two", 2)
    print(df)
    
    df = df.astype({"Start": int, "Last": float, "Seasons": int}) 
    # pd.to_numeric(df["Seasons"], downcast="integer")
    print(df.dtypes)
    return df

def main():
    cleaning_data()

if __name__ == "__main__":
    main()
