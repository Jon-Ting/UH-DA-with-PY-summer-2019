#!/usr/bin/env python3
 
def triple(x):
    return x*3
 
def square(x):
    return x**2
 
def main():
    for i in range(1, 11):
        t = triple(i)
        s = square(i)
        if s > t:
            break
        print("triple({0})=={1} square({0})=={2}".format(i, t, s))
 
if __name__ == "__main__":
    main()
 
