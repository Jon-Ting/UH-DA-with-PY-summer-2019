#!/usr/bin/env python3

import numpy as np

def diamond(n):
    diag_right = np.eye(n, dtype=int)
    diag_left = diag_right[:, ::-1]
    #print(diag_left, "\n\n", diag_right)
    top_half = np.concatenate((diag_left[:, 0:n-1], diag_right), axis=1)
    bot_half = np.concatenate((diag_right[1:, :], diag_left[1:, 1:]), axis=1)
    #print(top_half, bot_half)
    return_array = np.concatenate((top_half, bot_half))
    return return_array

def main():
    print(diamond(5))

if __name__ == "__main__":
    main()
