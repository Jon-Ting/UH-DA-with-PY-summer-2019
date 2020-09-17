#!/usr/bin/env python3
import numpy as np
import functools
import numpy.linalg as la

def matrix_power(a, n):
    if n == 0:
        a2 = np.eye(a.shape[0])
    elif n > 0:
        generator = (a for i in range(n-1))
        a2 = functools.reduce(np.matmul, list(generator)[:], a)
    else:
        generator = (la.inv(a) for i in range(abs(n)-1))
        #print(a@list(generator)[:])
        a2 = functools.reduce(np.matmul, list(generator)[:], la.inv(a))
    return a2

def main():
    a = np.array([[1, 2], [3, 4]])
    #print(a)
    print(matrix_power(a, -2))

if __name__ == "__main__":
    main()
