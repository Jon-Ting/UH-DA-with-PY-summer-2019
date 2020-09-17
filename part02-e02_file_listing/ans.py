#!/usr/bin/env python3
 
import re
 
 
def file_listing(filename="src/listing.txt"):
    with open(filename) as f:
        lines = f.readlines()
    result=[]
    for line in lines:
        pattern = r".{10}\s+\d+\s+.+\s+.+\s+(\d+)\s+(...)\s+(\d+)\s+(\d\d):(\d\d)\s+(.+)"
        if True:      # Two alternative ways of doing the same thing
            m = re.match(pattern, line)
        else:
            compiled_pattern = re.compile(pattern)
            m = compiled_pattern.match(line)
        if m:
            t = m.groups()
            result.append((int(t[0]), t[1], int(t[2]), int(t[3]), int(t[4]), t[5]))
        else:
            print(line)
    return result
 
def main():
    tuples = file_listing()
    for t in tuples:
        print(t)
 
if __name__ == "__main__":
    main()

