#!/usr/bin/env python3

import pandas as pd

def inverse_series(s):
    val_list, idx_list = [], []
    for i, idx in enumerate(s.index):
        idx_list.append(idx)
        val_list.append(s[idx])
    inv_s = pd.Series(idx_list, index=val_list)
    return inv_s

def main():
    a = pd.Series([1, 2, 3, 4], index=list("abcd"))
    print(inverse_series(a))
    # return

if __name__ == "__main__":
    main()
