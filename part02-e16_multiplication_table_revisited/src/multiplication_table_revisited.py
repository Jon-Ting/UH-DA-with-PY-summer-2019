#!/usr/bin/env python3

import numpy as np

def multiplication_table(n):
    a, b = np.arange(0, n).reshape(1, n), np.arange(0, n).reshape(n, 1)
    broadcasted_a, broadcasted_b = np.broadcast_arrays(a, b)
    return broadcasted_a * broadcasted_b

def main():
    print(multiplication_table(4))

if __name__ == "__main__":
    main()
