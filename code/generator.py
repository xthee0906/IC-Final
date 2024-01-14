# ==================================================================
# Copyright (c) 2024 National Tsing Hua University EE dept.
# Author: Tsung-Han Hsieh
# Description: Generator for RTL Bitstream Dataset
# ==================================================================

import cv2
import os
from functions.DCT import *
from functions.RGB2YCbCr import *
from functions.Quantization import *
from functions.dataset import *
from functions.value import *
from functions.checker import *


if not os.path.exists('dataset'): os.makedirs('dataset')
if not os.path.exists('dataset/Golden'): os.makedirs('dataset/Golden')
if not os.path.exists('dataset/ChannelValue'): os.makedirs('dataset/ChannelValue')
if not os.path.exists('dataset/ChannelValue/RGB'): os.makedirs('dataset/ChannelValue/RGB')
if not os.path.exists('dataset/ChannelValue/YCbCr'): os.makedirs('dataset/ChannelValue/YCbCr')
if not os.path.exists('dataset/ChannelValue/DCT'): os.makedirs('dataset/ChannelValue/DCT')
if not os.path.exists('dataset/ChannelValue/Q'): os.makedirs('dataset/ChannelValue/Q')
if not os.path.exists('dataset/BlockChecker'): os.makedirs('dataset/BlockChecker')

# 0 for cat 1 for number
type = 1 

# mode = 3 # fill bit
# mode = 2 # binary
# mode = 1 # output (correct form)
# mode = 0 # deciaml
mode = 1

image = cv2.resize(cv2.imread('../data/cat.bmp'), (256, 144))


get_RGB_value_forcheck(image)
get_RGB_dataset(image, mode = mode)
file_path = './dataset/Golden/SRAM_RGB.dat'
checkvalue(file_path, addr = 0)


image_YCbCr = rgb2ycrcb(image)
get_YCbCr_value_forcheck(image_YCbCr)
get_YCbCr_datset(image_YCbCr, mode = mode)
file_path = './dataset/Golden/SRAM_YCbCr.dat'
checkvalue(file_path, addr = 0)


DCT_image = DCT_matrix_ver(image_YCbCr)
get_DCT_value_forcheck(DCT_image)
get_DCT_datset(DCT_image, mode = mode)
file_path = './dataset/Golden/SRAM_DCT.dat'
checkvalue(file_path, addr = 0)


Q_image = Quantization(DCT_image, type)
get_Q_value_forcheck(Q_image)
get_Q_datset(Q_image, mode = mode)
file_path = './dataset/Golden/SRAM_Q.dat'
checkvalue(file_path, addr = 0)

RLC(Q_image)
file_path = './dataset/Golden/SRAM_F.dat'
checkvalue(file_path, addr = 0)

#   0
#  96
# 192
if (mode == 0):
    checkblock(0)
