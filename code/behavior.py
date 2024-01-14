# ==================================================================
# Copyright (c) 2024 National Tsing Hua University EE dept.
# Author: Tsung-Han Hsieh
# Description: JPEG Sofware Behavior for Hybrid Image
# ==================================================================

import cv2
import numpy as np
from functions.DCT import *
from functions.IDCT import *
from functions.RGB2YCbCr import *
from functions.Quantization import *


def hybrid(image, image1, mode):
    image_high = np.zeros_like(image).astype(int)
    iDCT_image_YCrCb = iDCT_matrix_hver(Quantization(DCT_matrix_ver(rgb2ycrcb(image)), mode), mode)
    iDCT_image = cv2.cvtColor(iDCT_image_YCrCb, cv2.COLOR_YCrCb2BGR)
    image_high = image.astype(int) - iDCT_image.astype(int)
    cv2.imshow('high', image_high.astype(np.uint8))

    image_low = np.zeros_like(image1).astype(int)
    image_YCbCr = rgb2ycrcb(image1)
    iDCT_image = iDCT_matrix_ver(Inverse_Quantization(Quantization(DCT_matrix_ver(image_YCbCr), mode),mode))
    iDCT_image = cv2.cvtColor(iDCT_image, cv2.COLOR_YCrCb2BGR)
    image_low = iDCT_image.astype(int)
    cv2.imshow('low', image_low.astype(np.uint8))

    return (image_high.astype(int) + image_low.astype(int)).clip(0, 255).astype(np.uint8)

#=========================== You can modified mode/image ============================
# 1 for number; 0 for cat
mode = 0

# Load the image with low frequency and image with high frequency
if mode == 0:
    image_low = cv2.resize(cv2.imread('../data/dog.bmp'), (256,144))
    image_high = cv2.resize(cv2.imread('../data/cat.bmp'), (256,144))
else:
    image_low = cv2.resize(cv2.imread('../data/EE4292.png'), (256,144))
    image_high = cv2.resize(cv2.imread('../data/number.png'), (256,144))
#=========================== You can modified mode/image ============================


#============================ JPEG Flow DON'T TOUCH !!! ============================
# image RGB to YCrCb
image_YCrCb = rgb2ycrcb(image_low)
# image YCrCb do Discrete Cosine Transform
DCT_image = DCT_matrix_ver(image_YCrCb)
# quantization
Q_image = Quantization(DCT_image, mode)
# dequantization
DCT_image = Inverse_Quantization(Q_image, mode)
# Inverse Discrete Cosine Transform
iDCT_image = iDCT_matrix_ver(DCT_image)
# image YCrCb to RGB
iDCT_image = cv2.cvtColor(iDCT_image, cv2.COLOR_YCrCb2BGR)
# Visualization
cv2.imshow('DCT', DCT_image.astype(np.uint8))
cv2.imshow('iDCT', iDCT_image)
cv2.imshow('Hybrid Image', hybrid(image_high,image_low,mode))
cv2.waitKey(0)
cv2.destroyAllWindows()
#============================ JPEG Flow DON'T TOUCH !!! ============================