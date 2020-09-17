#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt


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

    
def cyclists_per_day():
    cyclist = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    cyclist = split_date_continues(cyclist)
    # print(cyclist)
    groups = cyclist.groupby(by=["Year", "Month", "Day"], as_index=True)
    # for key, group in groups:
    #     print(key, len(group))
    # print(groups.get_group((2014, 1, 1)))
    # print(groups["Baana"].sum())
    df = groups.apply(lambda df : df.sum())
    # df = df.drop(columns=["Weekday", "Hour"])
    df = df.drop(columns=["Weekday", "Hour", "Year", "Month", "Day"])
    # df = groups.transform(lambda x : x.sum())  # Transfrom maintains the shape of df!
    # print(df)
    return df


def main():
    df = cyclists_per_day()
    # print(df.index)
    # print(df)
    august_days = list(range(1, 32))
    df = df.xs(2017)
    counts = df.xs(8)
    print(counts)
    plt.plot(august_days, counts)
    plt.show()


if __name__ == "__main__":
    main()
