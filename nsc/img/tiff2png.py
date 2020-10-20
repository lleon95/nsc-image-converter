#!/usr/bin/env python3
"""
.. module:: tiff2png
   :synopsis: Converts from TIFF in 12 bits to PNG
.. moduleauthor:: Luis G. Leon Vega <luis@luisleon.me>
"""

import argparse
import cv2 as cv
import numpy as np


def name_change(input_path):
    splitted_name = input_path.split('.tif')
    output_name = ''

    if len(splitted_name) == 2:
        output_name = splitted_name[0] + '.png'
    else:
        raise ValueError("The provided file is not a tiff file")

    return output_name


def convert(img_path, normalisation=2048):
    """
    **Tiff 12 image converter**

    :param img_path: path to the file
    :type img_path: string
    :param normalisation: max value within the image
    :type normalisation: int

    :return: OpenCV image in 8-bit grayscale format
    """
    # Read the image
    tiff = cv.imread(img_path, -1)

    if tiff is None:
        raise RuntimeError("Cannot load the image")
        return

    # Compute the image
    tiff = tiff.astype(np.float)
    tiff *= 255.0
    tiff /= normalisation
    tiff = tiff.astype(np.uint8)

    return tiff


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Converts the images from ARES to PNG")

    parser.add_argument(
        "--input", type=str, help="Location of the image", required=True
    )
    parser.add_argument(
        "--normalisation", type=int, help="Normalisation value", default=2048
    )

    args = parser.parse_args()

    # Get the output file name
    output_path = name_change(args.input)

    output_img = convert(args.input, args.normalisation)

    # Save the image
    cv.imwrite(output_path, output_img)
