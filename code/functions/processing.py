# ==================================================================
# Copyright (c) 2024 National Tsing Hua University EE dept.
# Author: Tsung-Han Hsieh
# Description: Data Processing for Decoder
# ==================================================================

import numpy as np

def CheckValue(image, channel):
    c = 0
    a = 0
    channel_values = image[:, :, channel]
    output_file_path = './result/channel_values.txt'
    with open(output_file_path, 'w') as file:
        for row in channel_values:
            for value in row:
                c = c + 1
                file.write(str(value).rjust(4) + ' ')
                if (c == 8):
                    file.write('||')
                    c = 0
            file.write('\n')
            a = a+1
            if (a == 8):
                file.write('-'*1024)
                file.write('\n')
                a = 0


def read_file(Table_code_path, Table_length_path, code_path, length_path, DC_code_path, DC_length_path):

    # read code and length table
    with open(Table_code_path, 'r') as file:
        Table_code = [int(line) for line in file.readlines()]
    with open(Table_length_path, 'r') as file:
        Tabel_len = [int(line) for line in file.readlines()]

    # read code value
    code_arrays = []
    with open(code_path, 'r') as file:
        lines = file.readlines()
    for line in lines:
        array = list(map(int, line.split()))
        code_arrays.append(array)

    # read DC length value
    with open(DC_length_path, 'r') as file:
        DC_len_array = [int(line) for line in file.readlines()]

    # read DC code value
    with open(DC_code_path, 'r') as file:
        DC_code_array = []
        c = 0
        for line in file.readlines():
            DC_code_array.append(line[-2:-(DC_len_array[c]+2):-1][::-1])
            c = c + 1

    # read length value
    len_arrays = []
    with open(length_path, 'r') as file:
        lines = file.readlines()
    for line in lines:
        array = list(map(int, line.split()))
        len_arrays.append(array)

    return Table_code, Tabel_len, code_arrays, len_arrays, DC_code_array

def read_table(Table_code_path, Table_length_path):
    # read code and length table
    with open(Table_code_path, 'r') as file:
        Table_code = [int(line) for line in file.readlines()]
    with open(Table_length_path, 'r') as file:
        Tabel_len = [int(line) for line in file.readlines()]

    return Table_code, Tabel_len

def read_AC(code_path, length_path):
    # read code value
    code_arrays = []
    with open(code_path, 'r') as file:
        lines = file.readlines()
    for line in lines:
        array = list(map(int, line.split()))
        code_arrays.append(array)

    # read length value
    len_arrays = []
    with open(length_path, 'r') as file:
        lines = file.readlines()
    for line in lines:
        array = list(map(int, line.split()))
        len_arrays.append(array)

    return code_arrays, len_arrays

def read_DC(DC_code_path, DC_length_path):
    # read DC length value
    with open(DC_length_path, 'r') as file:
        DC_len_array = [int(line) for line in file.readlines()]

    # read DC code value
    with open(DC_code_path, 'r') as file:
        DC_code_array = []
        c = 0
        for line in file.readlines():
            DC_code_array.append(line[-2:-(DC_len_array[c]+2):-1][::-1])
            c = c + 1

    return DC_code_array

def combineYCbCr(Q_image_Y, Q_image_Cb, Q_image_Cr):
    Q_image = np.zeros((144, 256, 3), dtype=int)
    Q_image[:,:,0] = Q_image_Y[:,:,0]
    Q_image[:,:,1] = Q_image_Cr[:,:,0]
    Q_image[:,:,2] = Q_image_Cb[:,:,0]
    return Q_image