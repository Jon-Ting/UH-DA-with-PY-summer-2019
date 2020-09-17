#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    return_list = []
    with open(filename, "r") as f:
        for i, line in enumerate(f.readlines()):
            if i == 0:
                continue
            else:
                colour_mo = re.findall(r"\d{1,3}", line)
                if len(colour_mo) > 3:
                    colour_mo = colour_mo[0:3]
                name_mo = re.findall(r"[A-Za-z]+\s?[a-z]*\s?[a-z]*", line.strip("\n"))
                all_mo = colour_mo + name_mo
                return_str = "\t".join(all_mo)
                #print(return_str)
                return_list.append(return_str)
    return return_list


def main():
    red_green_blue()

if __name__ == "__main__":
    main()
