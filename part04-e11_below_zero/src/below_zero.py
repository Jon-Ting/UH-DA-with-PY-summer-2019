#!/usr/bin/env python3

import pandas as pd

def below_zero():
    weather = pd.read_csv("src/kumpula-weather-2017.csv", sep=",")
    weather = weather[weather["Air temperature (degC)"] < 0]
    num_days = weather.shape[0]
    print("Number of days below zero: {0}".format(num_days))
    return num_days

def main():
    below_zero()
    
if __name__ == "__main__":
    main()
