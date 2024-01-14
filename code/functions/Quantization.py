# ==================================================================
# Copyright (c) 2024 National Tsing Hua University EE dept.
# Author: Tsung-Han Hsieh
# Description: Functions for Doing Quantization/Dequantization
# ==================================================================

import numpy as np

def Quantization(DCT_image, mode):
    if mode == 0:
        Q = np.array([
            [  16,  32,  64, 128, 512, 512, 512, 512],
            [ 32,  64, 512, 512, 512, 512, 512, 512],
            [ 64,  512, 512, 512, 512, 512, 512, 512],
            [512, 512, 512, 512, 512, 512, 512, 512],
            [512, 512, 512, 512, 512, 512, 512, 512],
            [512, 512, 512, 512, 512, 512, 512, 512],
            [512, 512, 512, 512, 512, 512, 512, 512],
            [512, 512, 512, 512, 512, 512, 512, 512]
        ]) # mode = 0 for cat

    else:
        Q = np.array([
            [  16,  64,  512, 512, 512, 512, 512, 512],
            [ 64,  512, 512, 512, 512, 512, 512, 512],
            [ 512,  512, 512, 512, 512, 512, 512, 512],
            [512, 512, 512, 512, 512, 512, 512, 512],
            [512, 512, 512, 512, 512, 512, 512, 512],
            [512, 512, 512, 512, 512, 512, 512, 512],
            [512, 512, 512, 512, 512, 512, 512, 512],
            [512, 512, 512, 512, 512, 512, 512, 512]
        ]) # new mode 1 for number
        
    image_height, image_width, image_channels = DCT_image.shape
    q_image = np.zeros_like(DCT_image).astype(int)
    
    for i in range(0, image_height, 8):
        for j in range(0, image_width, 8):
            for ch in range(image_channels):
                block = DCT_image[i:i+8, j:j+8, ch].astype(int)
                q_image[i:i+8, j:j+8, ch] = np.floor(block/Q + 0.5)

    return q_image

def Inverse_Quantization(DCT_image, mode):
    if mode == 0:
        Q = np.array([
            [  16,  32,  64, 128, 512, 512, 512, 512],
            [ 32,  64, 512, 512, 512, 512, 512, 512],
            [ 64,  512, 512, 512, 512, 512, 512, 512],
            [512, 512, 512, 512, 512, 512, 512, 512],
            [512, 512, 512, 512, 512, 512, 512, 512],
            [512, 512, 512, 512, 512, 512, 512, 512],
            [512, 512, 512, 512, 512, 512, 512, 512],
            [512, 512, 512, 512, 512, 512, 512, 512]
        ]) # mode = 0 for cat
    else:
        Q = np.array([
            [  16,  64,  512, 512, 512, 512, 512, 512],
            [ 64,  512, 512, 512, 512, 512, 512, 512],
            [ 512,  512, 512, 512, 512, 512, 512, 512],
            [512, 512, 512, 512, 512, 512, 512, 512],
            [512, 512, 512, 512, 512, 512, 512, 512],
            [512, 512, 512, 512, 512, 512, 512, 512],
            [512, 512, 512, 512, 512, 512, 512, 512],
            [512, 512, 512, 512, 512, 512, 512, 512]
        ]) # new mode 1 for number
    image_height, image_width, image_channels = DCT_image.shape
    q_image = np.zeros_like(DCT_image).astype(int)
    
    for i in range(0, image_height, 8):
        for j in range(0, image_width, 8):
            for ch in range(image_channels):
                block = DCT_image[i:i+8, j:j+8, ch].astype(int)
                q_image[i:i+8, j:j+8, ch] = np.floor(block*Q + 0.5)

    return q_image