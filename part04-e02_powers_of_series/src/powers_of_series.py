#!/usr/bin/env python3

import pandas as pd

def powers_of_series(s, k):
    first_col = s.values
    df_content = {}
    for i in range(k):
        i += 1
        df_content[i] = s.values ** i
    series_df = pd.DataFrame(df_content, index=s.index, columns=list(i+1 for i in range(k)))
    return series_df
    
def main():
    s = pd.Series([1,2,3,4], index=list("abcd"))
    print(powers_of_series(s, 3))
    
if __name__ == "__main__":
    main()
