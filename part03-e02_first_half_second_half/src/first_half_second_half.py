#!/usr/bin/env python3

import numpy as np

def first_half_second_half(a):
    m = int(a.shape[1]/2)
    # print(m)
    b, c = a[:, 0:m], a[:, m:]
    d = np.sum(b, axis=1) > np.sum(c, axis=1)
    print(b, c, d)
    return a[d]

def main():
    a = np.array([[1, 3, 4, 2], [2, 2, 1, 2]])
    print(first_half_second_half(a))

if __name__ == "__main__":
    main()
