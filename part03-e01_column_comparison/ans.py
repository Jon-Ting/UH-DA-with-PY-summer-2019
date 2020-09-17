#!/usr/bin/env python3
 
import numpy as np
 
def column_comparison(a):
    mask = a[:,1] > a[:,-2]
    return a[mask]
    
def main():
    np.random.seed(0)
    a=np.random.randn(10,10)
    np.set_printoptions(linewidth=1000)
    print("a:\n", a)
    print("result:\n", column_comparison(a))
 
if __name__ == "__main__":
    main()
 
