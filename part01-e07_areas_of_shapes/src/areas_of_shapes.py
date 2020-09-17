#!/usr/bin/env python3

import math


def main():
    # enter you solution here
    shape_list = ["triangle", "rectangle", "circle"]
    while True:
        shape = str(input("Choose a shape ({0}, {1}, {2}): ".format(shape_list[0], shape_list[1], shape_list[2])))
        if not shape:
            break
        elif shape not in shape_list:
            print("Unknown shape!")
            continue
        else:
            if shape == "triangle":
                base = float(input("Give base of the {0}: ".format(shape)))
                height = float(input("Give height of the {0}: ".format(shape)))
                area = base * height / 2
            elif shape == "rectangle":
                width = float(input("Give width of the {0}: ".format(shape)))
                height = float(input("Give height of the {0}: ".format(shape)))
                area = width * height
            elif shape == "circle":
                radius = float(input("Give radius of the {0}: ".format(shape)))
                area = math.pi * radius ** 2
            else:
                print("Something is wrong! Troubleshoot!")
                continue
            print(f"The area is {area:.6f}")
            

if __name__ == "__main__":
    main()
