#!/usr/bin/env python3

def interleave(*lists):
    return_list = []
    for i in zip(*lists):
        return_list.extend([*i])
    return return_list

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
