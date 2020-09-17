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
    series = pd.Series(data=grouped_df["mean"], index=grouped_df.index)
    return series

    
def suicide_weather():
    df1 = suicide_fractions()
    print(df1)
    
    df2 = pd.read_html("src/List_of_countries_by_average_yearly_temperature.html", index_col=0, header=0)[0]
    df2["Average yearly temperature (1961–1990, degrees Celsius)"] = df2["Average yearly temperature (1961–1990, degrees Celsius)"].str.replace("\u2212", "-")
    df2["Average yearly temperature (1961–1990, degrees Celsius)"] = df2["Average yearly temperature (1961–1990, degrees Celsius)"].astype(float)
    df2 = pd.Series(data=df2["Average yearly temperature (1961–1990, degrees Celsius)"], index=df2.index)
    print(df2)
    
    idx = df1.index.intersection(df2.index)
    # print(idx, len(idx))
    df3 =  df2[idx]  # common DataFrame
    # print(df3)

    spear_corr = df2.corr(df1, method="spearman")
    return (df1.shape[0], df2.shape[0], df3.shape[0], spear_corr)


def main():
    (suicide_rows, temp_rows, common_rows, spear_corr) = suicide_weather()
    print("Suicide DataFrame has {0} rows".format(suicide_rows))
    print("Temperature DataFrame has {0} rows".format(temp_rows))
    print("Common DataFrame has {0} rows".format(common_rows))
    print("Spearman correlation: {0:.1f}".format(spear_corr))


if __name__ == "__main__":
    main()
