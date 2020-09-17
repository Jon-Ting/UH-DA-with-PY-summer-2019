# Enter you module contents here
"""Triangle module"""
from math import sqrt

__author__ = "Jonathan Ting"
__version__ = "1.0"


def hypothenuse(x, y):
    """Returns the length of the hypothenuse given the lengths of two other sides of a right-angled triangle"""
    return sqrt(x ** 2 + y ** 2)

def area(x, y):
    """Returns the area of the right-angled triangle, given the two sides, perpendicular to each other"""
    return x * y / 2

def main():
    x, y = float(2), float(3)
    print(hypothenuse(x, y))
    print(area(x, y))

if __name__ == "__main__":
    main()
