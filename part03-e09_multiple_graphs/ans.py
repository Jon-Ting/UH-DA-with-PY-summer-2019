#!/usr/bin/env python3
 
import matplotlib.pyplot as plt
 
def main():
    plt.plot([2,4,6,7], [4,3,5,1], [1,2,3,4], [4,2,3,1])
    plt.xlabel("my x axis")
    plt.ylabel("my y axis")
    plt.show()
 
if __name__ == "__main__":
    main()
 
