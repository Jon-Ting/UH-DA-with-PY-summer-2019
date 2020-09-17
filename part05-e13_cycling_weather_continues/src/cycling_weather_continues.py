#!/usr/bin/env python3
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


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
    sum_cyclist = cyclist.groupby(["Year", "Month", "Day"]).sum()
    sum_cyclist = sum_cyclist.reset_index()
    # print(sum_cyclist, cyclist, weather)
    df = pd.merge(sum_cyclist, weather, how="inner", left_on=["Year", "Month", "Day"], right_on=["Year", "m", "d"])
    df = df.drop(["m", "d", "Time", "Time zone", "Hour"], axis=1)
    df = df.fillna(method="ffill")
    # print(df.isnull().any())
    print(df)
    return df


def cycling_weather_continues(station):
    df = cycling_weather()
    model = LinearRegression(fit_intercept=True)
    model.fit(df[["Precipitation amount (mm)", "Snow depth (cm)", "Air temperature (degC)"]], df[station])
    pred = model.predict(df[["Precipitation amount (mm)", "Snow depth (cm)", "Air temperature (degC)"]])
    # print(pred.shape, df[station].shape)
    coefficients = model.coef_
    score = model.score(df[["Precipitation amount (mm)", "Snow depth (cm)", "Air temperature (degC)"]], df[station])
    print(coefficients, score)
    return (coefficients, score)

    
def main():
    station = "Merikannontie"
    (coefficients, score) = cycling_weather_continues(station)
    print("Measuring station: {0}".format(station))
    print("Regression coefficient for variable 'precipitation': {0:.1f}".format(coefficients[0]))
    print("Regression coefficient for variable 'snow depth': {0:.1f}".format(coefficients[1]))
    print("Regression coefficient for variable 'temperature': {0:.1f}".format(coefficients[2]))
    print("Score: {0:.2f}".format(score))


if __name__ == "__main__":
    main()
