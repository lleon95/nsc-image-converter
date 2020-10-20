# Copyright 2020 - NanoSciTracker
# Author: Luis G. Leon Vega <luis@luisleon.me>

import unittest
import cv2 as cv
import numpy as np
import nsc.img.tiff2png as tiff2png

class test(unittest.TestCase):
    def test_convert_tiff2png(self):
        # Seed
        test_input = "./tests/Image2_10_2.tif"
        test_ref = "./tests/Image2_10_2.ref.png"

        # Open the reference
        ref = cv.imread(test_ref, 0)
        out = tiff2png.convert(test_input)
        
        print(ref.shape, out.shape)
        self.assertTrue(np.array_equal(ref, out))
