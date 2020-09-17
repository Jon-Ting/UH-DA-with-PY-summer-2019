#!/usr/bin/env python3
import pandas as pd


def create_series(L1, L2):
    idx_list = ['a', 'b', 'c']
    s1, s2 = pd.Series(L1, index=idx_list), pd.Series(L2, index=idx_list)
    return (s1, s2)
    
def modify_series(s1, s2):
    new_val = s2['b']
    s1['d'] = new_val
    del(s2['b'])
    return (s1, s2)
    
def main():
    a = [1, 2, 3]
    b = [4, 5, 6]
    (s1, s2) = create_series(a, b)
    (new_s1, new_s2) = modify_series(s1, s2)
    sum_series = new_s1 + new_s2
    # return
    
if __name__ == "__main__":
    main()
