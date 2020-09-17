#!/usr/bin/env python3
import re

def integers_in_brackets(s):
    mo1 = re.findall(r"\[\s*[+-]?\w*] *\]", s)
    new_s = []
    for i, strings in enumerate(mo1):
        mo2 = re.search(r"[A-Za-z]", strings)
        if not mo2:
            new_s.append(strings.strip("[").strip("]").strip())
    new_s = " ".join(new_s)
    mo3 = re.findall(r' ?[+-]?\d+ ?', new_s)
    return_list = [int(x) for x in mo3]
    return return_list

def main():
    print(integers_in_brackets("   afd [asd] [12 ] [a34]  [        -43 ]tt [+12]xxx!"))
    #print(integers_in_brackets(" afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx"))

if __name__ == "__main__":
    main()
