#!/usr/bin/env python3

import pandas as pd

def main():
    municipal = pd.read_csv("src/municipal.tsv", sep="\t")
    df = pd.DataFrame(municipal)
    print("Shape: {0},{1}".format(df.shape[0], df.shape[1]))
    print("Columns:")
    for i in df.columns:
        print(i)


if __name__ == "__main__":
    main()
