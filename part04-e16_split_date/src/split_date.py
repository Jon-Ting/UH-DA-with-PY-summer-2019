#!/usr/bin/env python3

import pandas as pd
import numpy as np


day_conversion = {"ma": "Mon", "ti": "Tue", "ke": "Wed", "to": "Thu", "pe": "Fri", "la": "Sat", "su": "Sun"}
month_conversion = {"tammi": 1, "helmi": 2, "maalis": 3, "huhti": 4, "touko": 5, "kesä": 6, "heinä": 7, "elo": 8, "syys": 9, "loka": 10, "marras": 11, "joulu": 12}
idx_list = ["Weekday", "Day", "Month", "Year", "Hour"]


def split_date():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df = df.dropna(how="all").dropna(how="all", axis=1)
    df = df["Päivämäärä"].str.split(expand=True)
    df = df.replace(to_replace=day_conversion)
    df = df.replace(to_replace=month_conversion)
    df.columns = idx_list
    df["Hour"] = df["Hour"].str.split(":", expand=True)
    for idx in idx_list:
        if idx == "Weekday": continue
        df[idx] = df[idx].map(int)
    print(df) 
    return df


def main():
    split_date()
   
      
if __name__ == "__main__":
    main()
