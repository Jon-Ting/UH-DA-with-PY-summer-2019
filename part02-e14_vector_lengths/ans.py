#!/usr/bin/env python3
 
import numpy as np
#import scipy.linalg
 
def vector_lengths(a):
    #return scipy.linalg.norm(a, 2, axis=1)
    return np.sqrt(np.sum(a**2, axis=1))
 
def main():
    a = np.asarray([[1, 2], [3, 4], [5, 6]])
    print("a:", a)
    print("Lengths:", vector_lengths(a))
 
if __name__ == "__main__":
    main()
