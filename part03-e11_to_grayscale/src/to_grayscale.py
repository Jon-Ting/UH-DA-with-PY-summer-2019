#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def to_grayscale(image_array):
    red_weight, green_weight, blue_weight = 0.2126, 0.7152, 0.0722
    # print(image_array.shape)
    gray_image = image_array[:, :, 0] * red_weight + image_array[:, :, 1] * green_weight + image_array[:, :, 2] * blue_weight
    # print(gray_image.shape)
    return gray_image


def to_red(image_array):
    new_array = image_array
    new_array[:, :, 1] = 0
    new_array[:, :, 2] = 0
    return new_array


def to_green(image_array):
    new_array = image_array
    new_array[:, :, 0] = 0
    new_array[:, :, 2] = 0
    return new_array


def to_blue(image_array):
    new_array = image_array
    new_array[:, :, 0] = 0
    new_array[:, :, 1] = 0
    return new_array


def main():
    image_array = plt.imread("src/painting.png")
    gray_image = to_grayscale(image_array)
    plt.gray
    plt.imshow(gray_image)

    plt.subplot(3, 1, 1)
    red_image = to_red(image_array)
    plt.imshow(red_image)
    plt.subplot(3, 1, 2)
    green_image = to_green(image_array)
    plt.imshow(green_image)
    plt.subplot(3, 1, 3)
    blue_image = to_blue(image_array)
    plt.imshow(blue_image)
    plt.show()

if __name__ == "__main__":
    main()
