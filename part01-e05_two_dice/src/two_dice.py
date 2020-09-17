#!/usr/bin/env python3

def main():
    for i in range(1,7):
        for j in range(1,7):
            sum = i + j
            if sum == 5:
                print("({0},{1})".format(i,j))
            else:
                continue

if __name__ == "__main__":
    main()
