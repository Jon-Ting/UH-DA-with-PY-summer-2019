#!/usr/bin/env python3

import pandas as pd

def suicide_fractions():
    df = pd.read_csv("src/who_suicide_statistics.csv")
    df["population"] = df["population"].astype(float)
    df["suicides_no"] = df["suicides_no"].astype(float)
    df["mean"] = df["suicides_no"]/df["population"]
    # print(df)
    df = df.drop(labels=["year", "sex", "age", "suicides_no", "population"], axis=1)
    grouped_df = df.groupby("country").mean()
    print(grouped_df)
    series = pd.Series(data=grouped_df["mean"])
    print(series)
    return series

def main():
    suicide_fractions()

if __name__ == "__main__":
    main()
