#!/usr/bin/env python3

import numpy as np
#import scipy.linalg

def vector_lengths(a):
    a2 = np.sqrt(np.sum(a ** 2, axis=1))
    return a2

def main():
    a = np.array([[-0.59601277, -0.77801031], [ 0.53272282, -0.30235778], [ 0.28371203, -1.29676917], [ 1.18962586,  0.92653497], [ 0.38072886, 0.37398519]])
    print(a)
    print(vector_lengths(a))

if __name__ == "__main__":
    main()
