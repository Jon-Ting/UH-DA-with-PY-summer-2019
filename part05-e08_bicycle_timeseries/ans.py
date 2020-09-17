#!/usr/bin/env python3
 
import pandas as pd
 
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
 
def bicycle_timeseries():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df = df.dropna(axis=0, how="all").dropna(axis=1, how="all")
    d = split_date(df)
    df["Date"] = pd.to_datetime(d[["Year", "Month", "Day", "Hour"]]) 
    df = df.drop("Päivämäärä", axis=1)
    df = df.set_index("Date")
    return df
 
 
def main():
    df = bicycle_timeseries()
    print("Shape:", df.shape)
    print("dtypes:", df.dtypes)
    print("columns:", df.columns)
    print(df.head())
 
if __name__ == "__main__":
    main()
 
