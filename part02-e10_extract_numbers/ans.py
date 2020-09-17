#!/usr/bin/env python3
 
def extract_numbers(s):
    result=[]
    for word in s.split():
        try:
            result.append(int(word))
        except ValueError:
            try:
                result.append(float(word))
            except ValueError:
                pass
    return result
 
def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))
 
if __name__ == "__main__":
    main()
 

