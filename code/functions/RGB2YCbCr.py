# ==================================================================
# Copyright (c) 2024 National Tsing Hua University EE dept.
# Author: Tsung-Han Hsieh
# Description: Functions for RGB-to-YCbCr Fixed Point Calculation
# ==================================================================

import numpy as np

def rgb2ycrcb(image):
    image_YCbCr = np.zeros_like(image).astype(int)
    R = image[:,:,2].astype(int)
    G = image[:,:,1].astype(int)
    B = image[:,:,0].astype(int)
    
    Y  = R*66  + G*129 + B*25 + 4096
    Cb = B*112 - R*38  - G*74 + 32768
    Cr = R*112 - G*94  - B*18 + 32768
    
    image_YCbCr[:,:,0] = np.floor(Y/256 + 0.5)
    image_YCbCr[:,:,2] = np.floor(Cb/256 + 0.5)
    image_YCbCr[:,:,1] = np.floor(Cr/256 + 0.5)

    return image_YCbCr.astype(np.uint8)