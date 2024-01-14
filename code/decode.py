# ==================================================================
# Copyright (c) 2024 National Tsing Hua University EE dept.
# Author: Tsung-Han Hsieh
# Description: Decoder for RTL Bitstream Output
# ==================================================================

import os
import cv2
from functions.IDCT import *
from functions.ACDCdecoder import *
from functions.processing import *

Table_code_Y , Table_len_Y  = read_table(Table_code_path = './output/code_table.txt', Table_length_path = './output/len_table.txt')
Table_code_Cb, Table_len_Cb = read_table(Table_code_path = './output/code_table_Cb.txt', Table_length_path = './output/len_table_Cb.txt')
Table_code_Cr, Table_len_Cr = read_table(Table_code_path = './output/code_table_Cr.txt', Table_length_path = './output/len_table_Cr.txt')
code_Y, len_Y = read_AC(code_path = './output/code.txt', length_path = './output/len.txt')
code_Cb, len_Cb = read_AC(code_path = './output/code_Cb.txt', length_path = './output/len_Cb.txt')
code_Cr, len_Cr = read_AC(code_path = './output/code_Cr.txt', length_path = './output/len_Cr.txt')
DC_code_Y = read_DC(DC_code_path = './output/code_DC.txt' , DC_length_path = './output/len_DC.txt')
DC_code_Cb = read_DC( DC_code_path = './output/code_DC_Cb.txt' , DC_length_path = './output/len_DC_Cb.txt')
DC_code_Cr = read_DC( DC_code_path = './output/code_DC_Cr.txt' , DC_length_path = './output/len_DC_Cr.txt')


DC_decimal_Y = DC_decoder(DC_code_Y)
Q_image_Y = AC_decoder(Table_code_Y, Table_len_Y, code_Y, len_Y, DC_decimal_Y)

DC_decimal_Cb = DC_decoder(DC_code_Cb)
Q_image_Cb = AC_decoder(Table_code_Cb, Table_len_Cb, code_Cb, len_Cb, DC_decimal_Cb)

DC_decimal_Cr = DC_decoder(DC_code_Cr)
Q_image_Cr = AC_decoder(Table_code_Cr, Table_len_Cr, code_Cr, len_Cr, DC_decimal_Cr)

Q_image = combineYCbCr(Q_image_Y, Q_image_Cb, Q_image_Cr)


# CheckValue(Q_image,2)
if not os.path.exists('result'): os.makedirs('result')


iDCT_image = iDCT_matrix_with_iQ(Q_image,0)
iDCT_image = cv2.cvtColor(iDCT_image, cv2.COLOR_YCrCb2BGR)
cv2.imwrite('./result/RTL_result.png', iDCT_image)
cv2.imshow('iDCT', iDCT_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
