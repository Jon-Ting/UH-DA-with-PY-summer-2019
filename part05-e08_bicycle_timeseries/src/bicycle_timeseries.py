#!/usr/bin/env python3

import pandas as pd


days = {"ma": "Mon", "ti": "Tue", "ke": "Wed", "to": "Thu", "pe": "Fri", "la": "Sat", "su": "Sun"}
months = {"tammi": 1, "helmi": 2, "maalis": 3, "huhti": 4, "touko": 5, "kesä": 6, "heinä": 7, "elo": 8, "syys": 9, "loka": 10, "marras": 11, "joulu": 12}
idx_list = ["Weekday", "Day", "Month", "Year", "Hour"] 


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
    df =  pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df = df.dropna(how="all").dropna(how="all", axis=1)
    print(df)
    date_df = split_date(df)
    date_df["Päivämäärä"] = pd.to_datetime(date_df[["Year", "Month", "Day", "Hour"]])
    date_df = date_df.drop(columns=["Year", "Month", "Day", "Weekday", "Hour"])
    df = pd.concat([date_df, df.iloc[:, 1:]], axis=1, sort=False)
    df = df.set_index("Päivämäärä")
    print(df)
    return df


def main():
    bicycle_timeseries()


if __name__ == "__main__":
    main()
