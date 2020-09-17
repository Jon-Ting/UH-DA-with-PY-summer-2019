#!/usr/bin/env python3

import numpy as np

def get_rows(a):
    return_list = []
    for i in range(a.shape[0]):
        return_list.append(a[i, :])
    return return_list

def get_columns(a):
    return_list = []
    for i in range(a.shape[1]):
        return_list.append(a.T[i, :])
    return return_list

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Rows:", get_rows(a))
    print("Columns:", get_columns(a))

if __name__ == "__main__":
    main()
