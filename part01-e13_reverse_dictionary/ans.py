#!/usr/bin/env python3
 
def reverse_dictionary(d):
    result = {}
    for key, value in d.items():
        for v in value:
            if v in result:
                result[v].append(key)
            else:
                result[v] = [key]
    return result
 
def main():
    d = {"move":["liikuttaa"], "hide":["piilottaa", "salata"]}
    print(d)
    print(reverse_dictionary(d))
 
    d = {"move":["liikuttaa"], "hide":["piilottaa", "salata"],
         "six" : ["kuusi"], "fir" : ["kuusi"]}
    print(d)
    print(reverse_dictionary(d))
 
if __name__ == "__main__":
    main()
 
