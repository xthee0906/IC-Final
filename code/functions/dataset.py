# ==================================================================
# Copyright (c) 2024 National Tsing Hua University EE dept.
# Author: Tsung-Han Hsieh
# Description: Functions for Generate Golden Dataset
# ==================================================================

def convert_to_binary(input_str):
    binary_str = ''
    for digit in input_str:
        binary_str += format(int(digit,16), '04b')
    return binary_str

def convert_to_binary_RR(input_str):
    binary_str = ''
    for digit in input_str:
        binary_str += format(int(digit,16), '03b')
    return binary_str

def get_RGB_dataset(image, mode):
    image_height, image_width, _ = image.shape
    output_file_path = './dataset/Golden/SRAM_RGB.dat'
    with open(output_file_path, 'w') as file:
        for i in range(0, image_height, 8):
            for j in range(0, image_width, 8):
                block_B = image[i:i+8, j:j+8, 0]
                block_G = image[i:i+8, j:j+8, 1]
                block_R = image[i:i+8, j:j+8, 2]
                for row_R in block_R:
                    for value_R in row_R:
                        if (mode == 3):
                            file.write(f'{bin(value_R)[2:].zfill(8)} ')
                        elif (mode == 2):
                            file.write(f'{bin(value_R)[2:]} ')
                        elif (mode == 1):
                            file.write(f'{bin(value_R)[2:].zfill(8)}')
                        else:
                            file.write(f'{value_R} ')
                file.write('\n')
                for row_G in block_G:
                    for value_G in row_G:
                        if (mode == 3):
                            file.write(f'{bin(value_G)[2:].zfill(8)} ')
                        elif (mode == 2):
                            file.write(f'{bin(value_G)[2:]} ')
                        elif (mode == 1):
                            file.write(f'{bin(value_G)[2:].zfill(8)}')
                        else:
                            file.write(f'{value_G} ')
                file.write('\n')
                for row_B in block_B:
                    for value_B in row_B:
                        if (mode == 3):
                            file.write(f'{bin(value_B)[2:].zfill(8)} ')
                        elif (mode == 2):
                            file.write(f'{bin(value_B)[2:]} ')
                        elif (mode == 1):
                            file.write(f'{bin(value_B)[2:].zfill(8)}')
                        else:
                            file.write(f'{value_B} ')
                file.write('\n')

def get_YCbCr_datset(image, mode):
    image_height, image_width, _ = image.shape
    output_file_path = './dataset/Golden/SRAM_YCbCr.dat'
    with open(output_file_path, 'w') as file:
        for i in range(0, image_height, 8):
            for j in range(0, image_width, 8):
                block_Y = image[i:i+8, j:j+8, 0]
                block_Cb = image[i:i+8, j:j+8, 2]
                block_Cr = image[i:i+8, j:j+8, 1]
                for row_Y in block_Y:
                    for value_Y in row_Y:
                        if (mode == 3):
                            file.write(f'{bin(value_Y)[2:].zfill(8)} ')
                        elif (mode == 2):
                            file.write(f'{bin(value_Y)[2:]} ')
                        elif (mode == 1):
                            file.write(f'{bin(value_Y)[2:].zfill(8)}')
                        else:
                            file.write(f'{value_Y} ')
                file.write('\n')
                for row_Cb in block_Cb:
                    for value_Cb in row_Cb:
                        if (mode == 3):
                            file.write(f'{bin(value_Cb)[2:].zfill(8)} ')
                        elif (mode == 2):
                            file.write(f'{bin(value_Cb)[2:]} ')
                        elif (mode == 1):
                            file.write(f'{bin(value_Cb)[2:].zfill(8)}')
                        else:
                            file.write(f'{value_Cb} ')
                file.write('\n')
                for row_Cr in block_Cr:
                    for value_Cr in row_Cr:
                        if (mode == 3):
                            file.write(f'{bin(value_Cr)[2:].zfill(8)} ')
                        elif (mode == 2):
                            file.write(f'{bin(value_Cr)[2:]} ')
                        elif (mode == 1):
                            file.write(f'{bin(value_Cr)[2:].zfill(8)}')
                        else:
                            file.write(f'{value_Cr} ')
                file.write('\n')

def get_DCT_datset(image, mode):
    image_height, image_width, _ = image.shape
    output_file_path = './dataset/Golden/SRAM_DCT.dat'
    with open(output_file_path, 'w') as file:
        for i in range(0, image_height, 8):
            for j in range(0, image_width, 8):
                block_Y = image[i:i+8, j:j+8, 0]
                block_Cb = image[i:i+8, j:j+8, 2]
                block_Cr = image[i:i+8, j:j+8, 1]
                for row_Y in block_Y:
                    for value_Y in row_Y:
                        if (mode == 3):
                            file.write(f'{bin(value_Y & int("1"*11, 2))[2:].zfill(11)} ')
                        elif (mode == 2):
                            file.write(f'{bin(value_Y & int("1"*11, 2))[2:]} ')
                        elif (mode == 1):
                            file.write(f'{bin(value_Y & int("1"*11, 2))[2:].zfill(11)}')
                        else:
                            file.write(f'{value_Y} ')
                file.write('\n')
                for row_Cb in block_Cb:
                    for value_Cb in row_Cb:
                        if (mode == 3):
                            file.write(f'{bin(value_Cb & int("1"*11, 2))[2:].zfill(11)} ')
                        elif (mode == 2):
                            file.write(f'{bin(value_Cb & int("1"*11, 2))[2:]} ')
                        elif (mode == 1):
                            file.write(f'{bin(value_Cb & int("1"*11, 2))[2:].zfill(11)}')
                        else:
                            file.write(f'{value_Cb} ')
                file.write('\n')
                for row_Cr in block_Cr:
                    for value_Cr in row_Cr:
                        if (mode == 3):
                            file.write(f'{bin(value_Cr & int("1"*11, 2))[2:].zfill(11)} ')
                        elif (mode == 2):
                            file.write(f'{bin(value_Cr & int("1"*11, 2))[2:]} ')
                        elif (mode == 1):
                            file.write(f'{bin(value_Cr & int("1"*11, 2))[2:].zfill(11)}')
                        else:
                            file.write(f'{value_Cr} ')
                file.write('\n')

def get_Q_datset(image, mode):
    image_height, image_width, _ = image.shape
    output_file_path = './dataset/Golden/SRAM_Q.dat'
    with open(output_file_path, 'w') as file:
        for i in range(0, image_height, 8):
            for j in range(0, image_width, 8):
                block_Y = image[i:i+8, j:j+8, 0]
                block_Cb = image[i:i+8, j:j+8, 2]
                block_Cr = image[i:i+8, j:j+8, 1]
                for row_Y in block_Y:
                    for value_Y in row_Y:
                        if (mode == 3):
                            file.write(f'{bin(value_Y & int("1"*11, 2))[2:].zfill(11)} ')
                        elif (mode == 2):
                            file.write(f'{bin(value_Y & int("1"*11, 2))[2:]} ')
                        elif (mode == 1):
                            file.write(f'{bin(value_Y & int("1"*11, 2))[2:].zfill(11)}')
                        else:
                            file.write(f'{value_Y} ')
                file.write('\n')
                for row_Cb in block_Cb:
                    for value_Cb in row_Cb:
                        if (mode == 3):
                            file.write(f'{bin(value_Cb & int("1"*11, 2))[2:].zfill(11)} ')
                        elif (mode == 2):
                            file.write(f'{bin(value_Cb & int("1"*11, 2))[2:]} ')
                        elif (mode == 1):
                            file.write(f'{bin(value_Cb & int("1"*11, 2))[2:].zfill(11)}')
                        else:
                            file.write(f'{value_Cb} ')
                file.write('\n')
                for row_Cr in block_Cr:
                    for value_Cr in row_Cr:
                        if (mode == 3):
                            file.write(f'{bin(value_Cr & int("1"*11, 2))[2:].zfill(11)} ')
                        elif (mode == 2):
                            file.write(f'{bin(value_Cr & int("1"*11, 2))[2:]} ')
                        elif (mode == 1):
                            file.write(f'{bin(value_Cr & int("1"*11, 2))[2:].zfill(11)}')
                        else:
                            file.write(f'{value_Cr} ')
                file.write('\n')

def RLC(Q_image):
    image_height, image_width, image_channels = Q_image.shape
    RR = []
    LL = []
    FF = []
    dc = []
    mode = 1
    
    for i in range(0, image_height, 8):
        for j in range(0, image_width, 8):
            for ch in range(image_channels):
                R = []
                L = []
                F = [1,1,1,1,1,1,1,1]
                pre = 0
                block = Q_image[i:i+8, j:j+8, ch].astype(int)
                seq = zig_zag(block)
                DC = seq[0]
                for k in range(1, 7):
                    if (seq[k] != 0):
                        R.append(k-pre-1)
                        L.append(seq[k])
                        pre = k
                while len(L) < 8:
                    L.append(0)
                    R.append(0)
                R = R[::-1]
                L = L[::-1]
                for p in range(8):
                    for r in range(p+1, 8):
                        if (F[r] != 0 and R[p] == R[r] and L[p] == L[r]): 
                            F[p] = F[p] + 1
                            F[r] = 0

                hex_list = [hex(i & 0xF)[2:].upper() for i in R]
                RRR = ''.join(hex_list)
                RR.append(RRR)

                hex_list = [hex(i & 0xF)[2:].upper() for i in L]
                LLL = ''.join(hex_list)
                LL.append(LLL)

                hex_list = [hex(i & 0xF)[2:].upper() for i in F]
                FFF = ''.join(hex_list)
                FF.append(FFF)
                dc.append(DC)
    
    output_file_path = './dataset/Golden/SRAM_F.dat'
    with open(output_file_path, 'w') as file:
        for addr in range(0,1728,3):
            if (mode == 3):
                file.write(f'{bin(dc[addr] & int("1"*11, 2))[2:].zfill(11)} ')
                file.write(f'{convert_to_binary_RR(RR[addr])} ')
                file.write(f'{convert_to_binary(LL[addr])} ')
                file.write(f'{convert_to_binary(FF[addr])} ')
            elif (mode == 2):
                file.write(f'{bin(dc[addr] & int("1"*11, 2))[2:]} ')
                file.write(f'{convert_to_binary_RR(RR[addr])} ')
                file.write(f'{convert_to_binary(LL[addr])} ')
                file.write(f'{convert_to_binary(FF[addr])} ')
            elif (mode == 1):
                file.write(f'{bin(dc[addr] & int("1"*11, 2))[2:].zfill(11)}')
                file.write(f'{convert_to_binary_RR(RR[addr])}')
                file.write(f'{convert_to_binary(LL[addr])}')
                file.write(f'{convert_to_binary(FF[addr])}')
            else:
                file.write(f'{dc[addr]} ')
                file.write(f'{(RR[addr])} ')
                file.write(f'{(LL[addr])} ')
                file.write(f'{(FF[addr])} ')
            file.write('\n')
        for addr in range(2,1728,3):
            if (mode == 3):
                file.write(f'{bin(dc[addr] & int("1"*11, 2))[2:].zfill(11)} ')
                file.write(f'{convert_to_binary_RR(RR[addr])} ')
                file.write(f'{convert_to_binary(LL[addr])} ')
                file.write(f'{convert_to_binary(FF[addr])} ')
            elif (mode == 2):
                file.write(f'{bin(dc[addr] & int("1"*11, 2))[2:]} ')
                file.write(f'{convert_to_binary_RR(RR[addr])} ')
                file.write(f'{convert_to_binary(LL[addr])} ')
                file.write(f'{convert_to_binary(FF[addr])} ')
            elif (mode == 1):
                file.write(f'{bin(dc[addr] & int("1"*11, 2))[2:].zfill(11)}')
                file.write(f'{convert_to_binary_RR(RR[addr])}')
                file.write(f'{convert_to_binary(LL[addr])}')
                file.write(f'{convert_to_binary(FF[addr])}')
            else:
                file.write(f'{dc[addr]} ')
                file.write(f'{(RR[addr])} ')
                file.write(f'{(LL[addr])} ')
                file.write(f'{(FF[addr])} ')
            file.write('\n')
        for addr in range(1,1728,3):
            if (mode == 3):
                file.write(f'{bin(dc[addr] & int("1"*11, 2))[2:].zfill(11)} ')
                file.write(f'{convert_to_binary_RR(RR[addr])} ')
                file.write(f'{convert_to_binary(LL[addr])} ')
                file.write(f'{convert_to_binary(FF[addr])} ')
            elif (mode == 2):
                file.write(f'{bin(dc[addr] & int("1"*11, 2))[2:]} ')
                file.write(f'{convert_to_binary_RR(RR[addr])} ')
                file.write(f'{convert_to_binary(LL[addr])} ')
                file.write(f'{convert_to_binary(FF[addr])} ')
            elif (mode == 1):
                file.write(f'{bin(dc[addr] & int("1"*11, 2))[2:].zfill(11)}')
                file.write(f'{convert_to_binary_RR(RR[addr])}')
                file.write(f'{convert_to_binary(LL[addr])}')
                file.write(f'{convert_to_binary(FF[addr])}')
            else:
                file.write(f'{dc[addr]} ')
                file.write(f'{(RR[addr])} ')
                file.write(f'{(LL[addr])} ')
                file.write(f'{(FF[addr])} ')
            file.write('\n')

def zig_zag(block):
    seq = []
    x = [0, 0, 1, 2, 1, 0, 0, 1, 2, 3, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 7, 6, 5, 4, 3, 4, 5, 6, 7, 7, 6, 5, 7, 6, 7]
    y = [0, 1, 0, 0, 1, 2, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 7, 6, 5, 4, 3, 2, 3, 4, 5, 6, 7, 7, 6, 5, 4, 5, 6, 7, 6, 7, 7]
    for i in range(64):
        seq.append(block[x[i]][y[i]])
    return seq

