#!/usr/bin/env python3
 
 
def main():
    for r in range(1, 11):
        for c in range(1, 11):
            print(f"{r*c:4d}", end="")
        print()
 
if __name__ == "__main__":
    main()
 
