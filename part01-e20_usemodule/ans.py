# -------------triangle.py--------------
"""Helper functions for triangles."""
 
__author__ = "Jarkko Toivonen"
__version__ = "1.0"
 
import math
 
def hypothenuse(a, b):
    """Computes the length of the hypothenuse of a right-angled triangle
with sides of length a and b."""
    return math.sqrt(a**2 + b**2)
 
def area(a, b):
    """Computes the area of a right-angled triangle
    with sides of length a and b."""
    return a*b/2




# -------------usemodule.py--------------
 #!/usr/bin/env python3
 
# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle
 
def main():
    print("The area is", triangle.area(4, 5))
    print("The hypothenuse is", triangle.hypothenuse(4, 5))
 
if __name__ == "__main__":
    main()
