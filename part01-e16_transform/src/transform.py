#!/usr/bin/env python3

def transform(s1, s2):
    L1, L2 = list(map(int, s1.split())), list(map(int, s2.split()))
    return_list = []
    for l1, l2 in zip(L1, L2):
        return_list.append(l1 * l2)
    return return_list

def main():
    print(transform("1 5 3", "2 6 -1"))

if __name__ == "__main__":
    main()
