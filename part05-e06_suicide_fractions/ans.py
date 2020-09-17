#!/usr/bin/env python3
 
import pandas as pd
 
def suicide_fractions():
    df = pd.read_csv("src/who_suicide_statistics.csv")
    df["Suicide fraction"] = df["suicides_no"] / df["population"]
    result = df.groupby("country").mean()
    return result["Suicide fraction"]
 
def main():
    df = suicide_fractions()
    print("Shape:", df.shape)
    print("Column name:", df.name)
    pd.set_option("display.max_rows", None)
    print(df)
    print(f"{df.isnull().sum()} missing values")
 
if __name__ == "__main__":
    main()
 
