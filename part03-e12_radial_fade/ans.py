#!/usr/bin/env python3
 
import numpy as np
import matplotlib.pyplot as plt
 
def center(a):
    return (a.shape[0]-1)/2, (a.shape[1]-1)/2
 
def radial_distance(a):
    cy, cx = center(a)
    x=np.abs(np.arange(a.shape[1])-cx)
    y=np.abs(np.arange(a.shape[0])-cy)
    X, Y = np.meshgrid(x, y)
    s = np.sqrt(X**2 + Y**2)
    return s
 
def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range
[tmin,tmax]."""
    min = np.min(a)
    max = np.max(a)
    a = (a - min) / (max - min)
    a = a * (tmax - tmin) + tmin
    return a
 
def radial_mask(a):
    s = radial_distance(a)
    if s.shape[0] <= 2 or s.shape[1] <= 2:
        return np.ones(s.shape)
    mask = scale(s)
    return 1 - mask
 
def radial_fade(a):
    m = radial_mask(a)[:,:,np.newaxis]
    return a*m
 
def main():
    np.set_printoptions(linewidth=1000)
    fig, ax = plt.subplots(3,1)
    a = plt.imread("src/painting.png")
    ax[0].set_title("Original")
    ax[0].imshow(a)
 
    mask = radial_mask(a)
    plt.gray()
    ax[1].set_title("Mask")
    ax[1].imshow(mask)
 
    result = radial_fade(a)
    ax[2].set_title("Faded")
    ax[2].imshow(result)
 
    fig.tight_layout()
    plt.show()
 
if __name__ == "__main__":
    main()
 
