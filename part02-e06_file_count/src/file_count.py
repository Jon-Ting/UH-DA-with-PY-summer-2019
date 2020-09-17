#!/usr/bin/env python3

import sys

def file_count(filename):
    num_word, num_line, num_char = 0, 0, 0
    with open(filename, "r") as f:
        for i, line in enumerate(f.readlines()):
            num_line += 1
            split_line = line.split()
            num_word += len(split_line)
            num_char += len(line)
    return (num_line, num_word, num_char)

def main():
    for i, filename in enumerate(sys.argv[1:]):
        (num_line, num_word, num_char) = file_count(filename)
        print(f"{num_line}\t{num_word}\t{num_char}\t{filename}")

if __name__ == "__main__":
    main()
