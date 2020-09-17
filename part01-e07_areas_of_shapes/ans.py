#!/usr/bin/env python3
 
import math
 
def triangle():
    base = float(input("Give base of the triangle: "))
    height = float(input("Give height of the triangle: "))
    return base * height / 2
 
def rect():
    base = float(input("Give width of the rectangle: "))
    height = float(input("Give height of the rectangle: "))
    return base * height
 
def circle():
    radius = float(input("Give radius of the circle: "))
    return math.pi*radius**2
 
def main():
    shape = input("Choose a shape (triangle, rectangle, circle): ")
    while shape:
        if shape == "triangle":
            output = f"The area is {triangle()}"
        elif shape == "rectangle":
            output = f"The area is {rect()}"
        elif shape == "circle":
            output = f"The area is {circle()}"
        else:
            output = "Unknown shape!"
        print(output)
        shape = input("Choose a shape (triangle, rectangle, circle): ")
 
if __name__ == "__main__":
    main()
 
