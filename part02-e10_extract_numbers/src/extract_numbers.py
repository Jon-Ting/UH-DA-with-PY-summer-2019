#!/usr/bin/env python3

def extract_numbers(s):
    return_list = []
    split_s = s.split()
    for i, entry in enumerate(split_s):
        try:
            entry = int(entry)
            return_list.append(entry)
        except (ValueError, ):
            try:
                entry = float(entry)
                return_list.append(entry)
            except (ValueError, ):
                continue 
    return return_list

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
