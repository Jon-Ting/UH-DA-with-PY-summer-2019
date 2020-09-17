#!/usr/bin/env python3
 
import re
 
def integers_in_brackets(s):
    result = re.findall(r"\[\s*([+-]?\d+)\s*\]", s)
    return list(map(int, result))
 
def main():
    print(integers_in_brackets("  afd [asd] \t[12 ] [a34]  [ -43 ]tt [+12]xxx"))
 
if __name__ == "__main__":
    main()
 
