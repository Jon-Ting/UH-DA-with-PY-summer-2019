#!/usr/bin/env python3

import pandas as pd

def average_temperature():
    weather = pd.read_csv("src/kumpula-weather-2017.csv", sep=",")
    weather = weather[weather["m"] == 7]
    avg_T = weather.mean()["Air temperature (degC)"]
    print("Average temperature in July: {0:.1f}".format(avg_T))
    return avg_T

def main():
    average_temperature()

if __name__ == "__main__":
    main()
