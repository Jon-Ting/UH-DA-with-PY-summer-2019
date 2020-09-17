#!/usr/bin/env python3

import numpy as np
import math
import sklearn.preprocessing as pp
import matplotlib.pyplot as plt
from scipy.spatial import distance


def center(a):
    center_y, center_x = (a.shape[0] - 1)/2, (a.shape[1] - 1)/2
    return (center_y, center_x)   # note the order: (center_y, center_x)

def radial_distance(a):
    height, width = a.shape[:2]
    center_coords = center(a)
    # print(center_coords)
    radial_mat = np.zeros((height, width))
    for i in range(height):
        for j in range(width):
            # euc_dist = math.sqrt((i - center_coords[0]) ** 2 + (j - center_coords[1]) ** 2)
            # euc_dist = np.linalg.norm(np.array(list(center_coords)) - np.array([i, j]))
            euc_dist = distance.euclidean(np.array(list(center_coords)), np.array([i, j]))
            radial_mat[i][j] = euc_dist
    return radial_mat

def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range
[tmin,tmax]."""
    '''
    '''
    #scaled_a = (a - np.min(a)) / (np.max(a) - np.min(a)) * (tmax - tmin)
    scaled_a = pp.minmax_scale(a, feature_range=(tmin, tmax))  # Doesn't seem to be radial
    return np.round(scaled_a, 5)

def radial_mask(a):
    radial_mat = radial_distance(a)
    # print(radial_mat.shape)
    scaled_mask = scale(radial_mat)
    # print(scaled_mask.shape)
    mask = np.array([1]) - scaled_mask
    # print(mask.shape)
    return mask

def radial_fade(a):
    mask = radial_mask(a).reshape((a.shape[0], a.shape[1], 1))
    mask = np.dstack((np.dstack((mask, mask)), mask))
    # print(mask.shape)
    faded_image = a * mask
    # print(faded_image.shape)
    return faded_image

def main():
    # print(center(np.zeros((10, 11, 3))))
    
    a = np.array([1]).reshape((1, 1))
    print(radial_mask(a))

    image_array = plt.imread("src/painting.png")
    plt.subplot(3, 1, 1)
    plt.imshow(image_array)
    
    mask = radial_mask(image_array)
    # print(mask)
    plt.subplot(3, 1, 2)
    plt.imshow(mask)
    
    faded_image = radial_fade(image_array)
    plt.subplot(3, 1, 3)
    plt.imshow(faded_image)
    plt.show()

if __name__ == "__main__":
    main()
