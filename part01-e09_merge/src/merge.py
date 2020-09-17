#!/usr/bin/env python3

def merge(L1, L2):
    L3 = L2
    for i, num1 in enumerate(L1):
        for j, num2 in enumerate(L2):
            if num1 < num2:
                continue
            else:
                L3.insert(j, num1)
    return L3

def main():
    L1 = sort(list(range(3)))
    L2 = sort(list(range(5)))
    print(merge(L1, L2))

if __name__ == "__main__":
    main()
