#!/usr/bin/env python3

import sys, math

def summary(filename):
    num_sum, num_line, mean_squared_sum = 0, 0, 0
    with open(filename, "r") as f:
        for i, line in enumerate(f.readlines()):
            try:
                num_sum += float(line.strip())
                num_line += 1
            except ValueError:
                continue
    num_avg = num_sum/num_line
    with open(filename, "r") as f:
        for i, line in enumerate(f.readlines()):
            try:
                number= float(line.strip())
                mean_squared = (number - num_avg)**2
                mean_squared_sum += mean_squared
            except ValueError:
                continue
    std_dev = math.sqrt(mean_squared_sum/(num_line - 1))
    return (num_sum, num_avg, std_dev)

def main():
    for i, filename in enumerate(sys.argv[1:]):
        (num_sum, num_avg, std_dev) = summary(filename)
        print(f"File: {filename} Sum: {num_sum:6f} Average: {num_avg:6f} Stddev: {std_dev:6f}")

if __name__ == "__main__":
    main()
