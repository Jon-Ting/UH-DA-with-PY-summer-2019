#!/usr/bin/env python3
 
def main():
    for a in range(1, 7):
        for b in range(1, 7):
            if a+b == 5:
                print(f"({a},{b})")
 
if __name__ == "__main__":
    main()
