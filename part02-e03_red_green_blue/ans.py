#!/usr/bin/env python3
 
import re
 
def red_green_blue(filename="src/rgb.txt"):
    with open(filename) as in_file:
        l = re.findall(r"(\d+)\s+(\d+)\s+(\d+)\s+(.*)\n", in_file.read())
        return [
            "{}\t{}\t{}\t{}".format(r, g, b, name)
            for r, g, b, name
            in l
        ]
 
 
def main():
    lines = red_green_blue()
    for line in lines:
        print(line)
 
if __name__ == "__main__":
    main()
 
