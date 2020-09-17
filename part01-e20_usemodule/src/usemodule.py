#!/usr/bin/env python3

# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle

def main():
    # Call the functions from here
    x, y = float(2), float(3)
    print(triangle.hypothenuse(x, y))
    print(triangle.area(x, y))

if __name__ == "__main__":
    main()
