# ==================================================================
# Copyright (c) 2024 National Tsing Hua University EE dept.
# Author: Tsung-Han Hsieh
# Description: Functions for Doing Inverse Discrete Cosine Transform
# ==================================================================

import numpy as np

def dct_matrix():
    dct_mat = np.zeros((8, 8))
    dct_mat = np.array([[5793, 5793, 5793, 5793, 5793, 5793, 5793, 5793],
                        [8035, 6811, 4551, 1598,-1598,-4551,-6811,-8035],
                        [7568, 3135,-3135,-7568,-7568,-3135, 3135, 7568],
                        [6811,-1598,-8035,-4551, 4551, 8035, 1598,-6811],
                        [5793,-5793,-5793, 5793, 5793,-5793,-5793, 5793],
                        [4551,-8035, 1598, 6811,-6811,-1598, 8035,-4551],
                        [3135,-7568, 7568,-3135,-3135, 7568,-7568, 3135],
                        [1598,-4551, 6811,-8035, 8035,-6811, 4551,-1598]])
    return dct_mat

def iDCT(block):
    dct_matrix_8x8 = dct_matrix()
    block_dct_1 = block @ dct_matrix_8x8
    block_dct_rounded_1 = np.floor(block_dct_1/16384 + 0.5)
    block_dct_2 = dct_matrix_8x8.T @ block_dct_rounded_1
    block_dct_rounded_2 = np.floor(block_dct_2/16384 + 0.5)
    block_dct_rounded_2 = block_dct_rounded_2 + 128

    return block_dct_rounded_2

def iDCT_matrix_ver(image_DCT):
    image_height, image_width, image_channels = image_DCT.shape
    idct_image = np.zeros_like(image_DCT).astype(int)
    
    for i in range(0, image_height, 8):
        for j in range(0, image_width, 8):
            for ch in range(image_channels):
                block = image_DCT[i:i+8, j:j+8, ch].astype(int)
                idct_image[i:i+8, j:j+8, ch] = iDCT(block)
            
    return idct_image.astype(np.uint8)

def iDCT_matrix_hver(image_DCT, mode):
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
    image_height, image_width, image_channels = image_DCT.shape
    idct_image = np.zeros_like(image_DCT).astype(int)
    
    for i in range(0, image_height, 8):
        for j in range(0, image_width, 8):
            for ch in range(image_channels):
                block = image_DCT[i:i+8, j:j+8, ch].astype(int)
                if mode == 0: block = block * (Q*3/5)
                else: block = block * Q
                idct_image[i:i+8, j:j+8, ch] = iDCT(block)
            
    return idct_image.astype(np.uint8)

def iDCT_matrix_with_iQ(image_DCT, mode):
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
    image_height, image_width, image_channels = image_DCT.shape
    idct_image = np.zeros_like(image_DCT).astype(int)
    
    for i in range(0, image_height, 8):
        for j in range(0, image_width, 8):
            for ch in range(image_channels):
                block = image_DCT[i:i+8, j:j+8, ch].astype(int)
                block = block * Q
                idct_image[i:i+8, j:j+8, ch] = iDCT(block)
            
    return idct_image.astype(np.uint8)
