#!/usr/bin/env python3
 
import pandas as pd
 
def read_series():
    values=[]
    indices=[]
    while True:
        line = input("")
        if not line:
            break
        i, v = line.split()
        values.append(v)
        indices.append(i)
    s = pd.Series(values, index=indices)
    return s
 
def main():
    print(read_series())
 
if __name__ == "__main__":
    main()
 
