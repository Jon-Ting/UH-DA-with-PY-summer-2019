#!/usr/bin/env python3

def find_matching(L, pattern):
    index_list = []
    for i, strings in enumerate(L):
        if pattern in strings:
            index_list.append(i)
    return index_list

def main():
    find_matching(["sensitive", "engine", "rubbish", "comment"], "en")
    pass

if __name__ == "__main__":
    main()
