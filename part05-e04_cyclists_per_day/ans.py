#!/usr/bin/env python3
 
import pandas as pd
import matplotlib.pyplot as plt
 
days = dict(zip("ma ti ke to pe la su".split(), "Mon Tue Wed Thu Fri Sat Sun".split()))
months = dict(zip("tammi helmi maalis huhti touko kesä heinä elo syys loka marras joulu".split(), range(1, 13)))
 
def split_date(df):
    d = df["Päivämäärä"].str.split(expand=True)
    d.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
 
    hourmin = d["Hour"].str.split(":", expand=True)
    d["Hour"] = hourmin.iloc[:, 0]
 
    d["Weekday"] = d["Weekday"].map(days)
    d["Month"] = d["Month"].map(months)
    
    d = d.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})
    return d
 
def split_date_continues():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df = df.dropna(axis=0, how="all").dropna(axis=1, how="all")
    d = split_date(df)
    df = df.drop("Päivämäärä", axis=1)
    return pd.concat([d, df], axis=1)
 
def cyclists_per_day():
    df = split_date_continues()
    res = df.groupby(["Year", "Month", "Day"]).sum()
    res = res.drop(["Hour"], axis=1)
    return res
    
def main():
    df = cyclists_per_day()
    print("Shape:", df.shape)
    print("Columns types:", df.dtypes)
    df = df.loc[(2017, 8), :]
    df.plot()
    plt.show()
 
if __name__ == "__main__":
    main()
 
