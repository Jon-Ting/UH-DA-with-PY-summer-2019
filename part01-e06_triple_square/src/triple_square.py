#!/usr/bin/env python3


def triple(inp):
    return inp*3


def square(inp):
    return inp**2


def main():
    for i in range(1,11):
        sq = square(i); tr = triple(i)
        if sq <= tr:
            print("triple({0})=={1} square({0})=={2}".format(i, tr, sq))
        else:
            break

if __name__ == "__main__":
    main()
