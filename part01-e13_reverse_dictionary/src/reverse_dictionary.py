#!/usr/bin/env python3

def reverse_dictionary(d):
    reverse_dict = {}
    for key, values in d.items():
        for value in values:
            if value in reverse_dict:
                pass
            else:
                reverse_dict[value] = []
            reverse_dict[value].append(key)
    return reverse_dict

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))

if __name__ == "__main__":
    main()
