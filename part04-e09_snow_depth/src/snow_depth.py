#!/usr/bin/env python3

import pandas as pd

def snow_depth():
    weather = pd.read_csv("src/kumpula-weather-2017.csv", sep=",")
    max_snow = weather.max()["Snow depth (cm)"]
    print("Max snow depth: {0:.1f}".format(max_snow))
    return max_snow

def main():
    snow_depth()

if __name__ == "__main__":
    main()
