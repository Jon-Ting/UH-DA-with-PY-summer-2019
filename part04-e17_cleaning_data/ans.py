#!/usr/bin/env python3
 
import pandas as pd
import numpy as np
 
def fix_name_field(s):
    s = s.str.replace(r"(\w+), *(\w+)", r"\2 \1")
    return s
 
def cleaning_data():
    df = pd.read_csv("src/presidents.tsv", sep="\t")
    df = df.where(df != "two", 2)
    df['Start'] = df['Start'].str.extract(r'^(\d{4})', expand=False)
    df = df.where(df != "-", np.nan)
 
    df["President"] = fix_name_field(df["President"])
    df["Vice-president"] = fix_name_field(df["Vice-president"]).str.title()
    return df.astype({"President":object, "Start":int,  "Last":float,
                      "Seasons":int, "Vice-president": object})
 
def main():
    df = cleaning_data()
    print("dtypes:", df.dtypes)
    print(df)
 
if __name__ == "__main__":
    main()
 
