#!/usr/bin/env python3

def distinct_characters(L):
    return_dict = {}
    for i, strings in enumerate(L):
        distinct_set = set(strings)
        return_dict[strings] = len(distinct_set)
    return return_dict

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
