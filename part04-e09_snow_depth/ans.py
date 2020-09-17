#!/usr/bin/env python3
 
import pandas as pd
 
def snow_depth():
    df = pd.read_csv("src/kumpula-weather-2017.csv")
    return df["Snow depth (cm)"].max()
 
def main():
    max_depth = snow_depth()
    print(f"Max snow depth: {max_depth:.1f}")
 
if __name__ == "__main__":
    main()
 
