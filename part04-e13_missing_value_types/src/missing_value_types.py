#!/usr/bin/env python3

import pandas as pd
import numpy as np

def missing_value_types():
    indep_list = [np.nan, 1917, 1776, 1523, np.nan,1992]
    pres_list = [None, "Niinistö", "Trump", None, "Steinmeier", "Putin"]
    state_list = ["United Kingdom", "Finland", "USA", "Sweden", "Germany", "Russia"]
    df = pd.DataFrame({"State": state_list, "Year of independence": indep_list, "President": pres_list})
    df = df.set_index("State")
    return df
               
def main():
    print(missing_value_types())

if __name__ == "__main__":
    main()
