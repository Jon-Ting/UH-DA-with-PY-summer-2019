#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    return_list = []
    with open(filename, "r") as f:
        for i, line in enumerate(f.readlines()):
            size_mo = int(re.findall(r"\d{2,}", line)[0])
            month_mo = re.findall(r"[A-Z][a-z]{2}", line)[0]
            day_mo = int(re.findall(r"\s?[1-3]?[0-9]\b", line)[-3])
            time_mo = re.findall(r"\d\d:\d\d", line)
            name_mo = re.findall(r"[\w\.]+", line)[-1]
            hour_mo, min_mo = int(re.split(":", time_mo[0])[0]), int(re.split(":", time_mo[0])[1])
            return_tuple = (size_mo, month_mo, day_mo, hour_mo, min_mo, name_mo)
            return_list.append(return_tuple)
    return return_list

def main():
    file_listing()

if __name__ == "__main__":
    main()
