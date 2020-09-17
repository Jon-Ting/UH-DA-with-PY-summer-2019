#!/usr/bin/env python3
 
import pandas as pd
 
def average_temperature():
    df = pd.read_csv("src/kumpula-weather-2017.csv", sep=",")
    m = df["m"] == 7
    return df[m]["Air temperature (degC)"].mean()
 
def main():
    t = average_temperature()
    print(f"Average temperature in July: {t:.1f}")
 
if __name__ == "__main__":
    main()

