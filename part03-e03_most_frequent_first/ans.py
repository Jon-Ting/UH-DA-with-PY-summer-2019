#!/usr/bin/env python3
 
import numpy as np
 
def most_frequent_first(a, c):
    b = a[:,c]   # get column c
    _,s,t = np.unique(b, return_inverse=True, return_counts=True)
    idx = np.argsort(t[s])
    return a[idx][::-1]
 
def main():
    np.random.seed(0)
    a = np.random.randint(0,10, (10,10))
    print("a:\n", a)
    print("result:\n", most_frequent_first(a, -1))
 
if __name__ == "__main__":
    main()
 
