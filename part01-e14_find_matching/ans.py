#!/usr/bin/env python3
 
def find_matching(L, pattern):
    result = []
    for i, s in enumerate(L):
        if pattern in s:
            result.append(i)
    return result
 
def main():
    result = find_matching(["sensitive", "engine", "rubbish", "comment"], "en")
    print(result)
 
if __name__ == "__main__":
    main()
 
