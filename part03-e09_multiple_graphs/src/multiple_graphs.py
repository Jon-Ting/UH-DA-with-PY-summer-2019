#!/usr/bin/env python3

import matplotlib.pyplot as plt

def main():
    x1, x2, y1, y2 = [2, 4, 6, 7], [1, 2, 3, 4], [4, 3, 5, 1], [4, 2, 3, 1]
    plt.plot(x1, y1, x2, y2)
    plt.title('Multiple Graphs')
    plt.xlabel('X-Axis'); plt.ylabel('Y-Axis')
    plt.show()

if __name__ == "__main__":
    main()
