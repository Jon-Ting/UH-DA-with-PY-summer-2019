#!/usr/bin/env python3

import numpy as np

def column_comparison(a):
    col1, col2 = a[:, 1].reshape(a.shape[0], 1), a[:, -2].reshape(a.shape[0], 1)
    b = np.concatenate((col1, col2), axis=1)
    c = b[:, 0] > b[:, 1]
    print(c)
    d = a[c]
    return d
    
def main():
    a = np.arange(0, 25).reshape(5, 5)
    print(a)
    print(column_comparison(a))
    
if __name__ == "__main__":
    main()
