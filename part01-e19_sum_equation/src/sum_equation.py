#!/usr/bin/env python3

def sum_equation(L):
    left = [str(x) for x in L]
    left = " + ".join(left)
    return_str = " ".join([left, "=", str(sum(L))])
    if len(L) == 0:
        return_str = "0" + return_str
    return return_str

def main():
    print(sum_equation([]))
    print(sum_equation([1,5,7]))

if __name__ == "__main__":
    main()
