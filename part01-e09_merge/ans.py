#!/usr/bin/env python3
 
def merge(L1, L2):
    result = []
    i, j = 0, 0
    # i = j = 0 would also work but leads to bad behaviour with mutable types so not recommended.
    while i < len(L1) and j < len(L2):
        if L1[i] <= L2[j]:
            result.append(L1[i])
            i += 1
        else:
            result.append(L2[j])
            j += 1
    if i < len(L1):
        result.extend(L1[i:])
    else:
        result.extend(L2[j:])
    return result
 
def main():
    print(merge([1, 5, 9, 12], [2, 6, 10]))
 
if __name__ == "__main__":
    main()
 
