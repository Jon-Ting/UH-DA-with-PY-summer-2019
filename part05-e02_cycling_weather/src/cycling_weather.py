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

def split_date_continues(df):
    df = df.dropna(how="all").dropna(how="all", axis=1)
    df1 = split_date(df)
    df2 = df.drop(labels=["Päivämäärä"], axis=1)
    df = pd.concat([df1, df2], axis=1, sort=False)
    return df


def cycling_weather():
    cyclist = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    cyclist = split_date_continues(cyclist)
    weather = pd.read_csv("src/kumpula-weather-2017.csv")
    df = pd.merge(cyclist, weather, how="inner", left_on=["Year", "Month", "Day"], right_on=["Year", "m", "d"])
    df = df.drop(["m", "d", "Time", "Time zone"], axis=1)
    print(df.index)
    print(df.columns)
    print(df)
    return df

def main():
    cycling_weather()

if __name__ == "__main__":
    main()
