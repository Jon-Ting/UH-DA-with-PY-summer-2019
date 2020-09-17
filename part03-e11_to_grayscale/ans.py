#!/usr/bin/env python3
 
import numpy as np
import matplotlib.pyplot as plt
 
 
def to_grayscale(image):
    w=np.array([0.2126, 0.7152, 0.0722]).reshape(1, 1, 3)
    a = image * w
    return a.sum(axis=2)
 
def to_red(image):
    image2=image.copy()
    image2[:,:,[1,2]] = 0
    return image2
 
def to_green(image):
    image2=image.copy()
    image2[:,:,[0,2]] = 0
    return image2
 
def to_blue(image):
    image2=image.copy()
    image2[:,:,[0,1]] = 0
    return image2
 
def main():
    painting=plt.imread("src/painting.png")
    gray = to_grayscale(painting)
    red = to_red(painting)
    green = to_green(painting)
    blue = to_blue(painting)
    plt.imshow(painting)
    plt.figure()
    plt.gray()
    plt.imshow(gray)
    plt.subplot(3, 1, 1)
    plt.imshow(red)
    plt.subplot(3, 1, 2)
    plt.imshow(green)
    plt.subplot(3, 1, 3)
    plt.imshow(blue)
    plt.show()
 
if __name__ == "__main__":
    main()
 
