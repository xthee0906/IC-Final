# ==================================================================
# Copyright (c) 2024 National Tsing Hua University EE dept.
# Author: Tsung-Han Hsieh
# Description: AC and DC Decoder for RTL Bitstream Output
# ==================================================================

import numpy as np

def hex_to_decimal_4bit(hex_value):
    decimal_value = int(hex_value, 16)

    if decimal_value & 0b1000:
        inverted_bits = ((decimal_value ^ 0b1111) + 1) & 0b1111
        decimal_value = -inverted_bits

    return decimal_value

def get_RL(code_table, code_out, len_table, code_len):
    # number of table is 128
    for i in range(128):
        for j in range(128):
            if (code_table[i] == code_out and len_table[j] == code_len and i == j):
                R = i//16
                L = hex(i%16)[2:]
                # print('(' + str(R)+','+ str(L) + ')', end=' ')
    return R, L

def getZigZag(code_table, len_table, code_arrays, len_arrays,block_number):
    zig_zag = []
    for code_number in range(8):
        code_len = len_arrays[block_number][code_number]
        code_out = code_arrays[block_number][code_number]
        R, L = get_RL(code_table, code_out, len_table, code_len)
        if (R == 0 and L == 0): zig_zag.append(0)
        if (R == 0 and L != 0): zig_zag.append(hex_to_decimal_4bit(L))
        if (R == 1 and L != 0): 
            zig_zag.append(0)
            zig_zag.append(hex_to_decimal_4bit(L))
        if (R == 2 and L != 0):
            zig_zag.extend([0, 0])
            zig_zag.append(hex_to_decimal_4bit(L))
        if (R == 3 and L != 0):
            zig_zag.extend([0, 0, 0])
            zig_zag.append(hex_to_decimal_4bit(L))
        if (R == 4 and L != 0):
            zig_zag.extend([0, 0, 0, 0])
            zig_zag.append(hex_to_decimal_4bit(L))
        if (R == 5 and L != 0):
            zig_zag.extend([0, 0, 0, 0, 0])
            zig_zag.append(hex_to_decimal_4bit(L))
        if (R == 6 and L != 0):
            zig_zag.extend([0, 0, 0, 0, 0, 0])
            zig_zag.append(hex_to_decimal_4bit(L))
        if (R == 7 and L != 0):
            zig_zag.extend([0, 0, 0, 0, 0, 0, 0])
            zig_zag.append(hex_to_decimal_4bit(L))
    
    return zig_zag


def AC_decoder(code_table, len_table, code_arrays, len_arrays, DC_decimal):
    block = np.zeros((144, 256, 3), dtype=int)
    for block_number in range(576):
        zig_zag = getZigZag(code_table, len_table, code_arrays, len_arrays, block_number)
        
        # Zig-Zag to block
        block[8*(block_number//32)  , (block_number*8)%256] = DC_decimal[block_number]
        block[8*(block_number//32)  , (block_number*8)%256+1] = zig_zag[0]
        block[8*(block_number//32)+1, (block_number*8)%256] = zig_zag[1]
        block[8*(block_number//32)+2, (block_number*8)%256] = zig_zag[2]
        block[8*(block_number//32)+1, (block_number*8)%256+1] = zig_zag[3]
        block[8*(block_number//32), (block_number*8)%256+2] = zig_zag[4]
        block[8*(block_number//32), (block_number*8)%256+3] = zig_zag[5]
        block[8*(block_number//32)+1, (block_number*8)%256+2] = zig_zag[6]
        block[8*(block_number//32)+2, (block_number*8)%256+1] = zig_zag[7]
    return block

def DC_decoder(DC_code_array):
    DC_decimal = []
    for block_number in range(576):
        if (DC_code_array[block_number][0:2] == '00'): DC_decimal.append(0)
        elif (DC_code_array[block_number][0:3] == '010'):
            if (DC_code_array[block_number][3] == '1'): DC_decimal.append(1)
            else: DC_decimal.append(-1)
        elif (DC_code_array[block_number][0:3] == '011'):
            if   (DC_code_array[block_number][3:5] == '00'): DC_decimal.append(-3)
            elif (DC_code_array[block_number][3:5] == '01'): DC_decimal.append(-2)
            elif (DC_code_array[block_number][3:5] == '10'): DC_decimal.append(2)
            elif (DC_code_array[block_number][3:5] == '11'): DC_decimal.append(3)
        elif (DC_code_array[block_number][0:3] == '100'):
            if   (DC_code_array[block_number][3:6] == '000'): DC_decimal.append(-7)
            elif (DC_code_array[block_number][3:6] == '001'): DC_decimal.append(-6)
            elif (DC_code_array[block_number][3:6] == '010'): DC_decimal.append(-5)
            elif (DC_code_array[block_number][3:6] == '011'): DC_decimal.append(-4)
            elif (DC_code_array[block_number][3:6] == '100'): DC_decimal.append(4)
            elif (DC_code_array[block_number][3:6] == '101'): DC_decimal.append(5)
            elif (DC_code_array[block_number][3:6] == '110'): DC_decimal.append(6)
            elif (DC_code_array[block_number][3:6] == '111'): DC_decimal.append(7)
        elif (DC_code_array[block_number][0:3] == '101'):
            if   (DC_code_array[block_number][3:7] == '0000'): DC_decimal.append(-15)
            elif (DC_code_array[block_number][3:7] == '0001'): DC_decimal.append(-14)
            elif (DC_code_array[block_number][3:7] == '0010'): DC_decimal.append(-13)
            elif (DC_code_array[block_number][3:7] == '0011'): DC_decimal.append(-12)
            elif (DC_code_array[block_number][3:7] == '0100'): DC_decimal.append(-11)
            elif (DC_code_array[block_number][3:7] == '0101'): DC_decimal.append(-10)
            elif (DC_code_array[block_number][3:7] == '0110'): DC_decimal.append(-9)
            elif (DC_code_array[block_number][3:7] == '0111'): DC_decimal.append(-8)
            elif (DC_code_array[block_number][3:7] == '1000'): DC_decimal.append(8)
            elif (DC_code_array[block_number][3:7] == '1001'): DC_decimal.append(9)
            elif (DC_code_array[block_number][3:7] == '1010'): DC_decimal.append(10)
            elif (DC_code_array[block_number][3:7] == '1011'): DC_decimal.append(11)
            elif (DC_code_array[block_number][3:7] == '1100'): DC_decimal.append(12)
            elif (DC_code_array[block_number][3:7] == '1101'): DC_decimal.append(13)
            elif (DC_code_array[block_number][3:7] == '1110'): DC_decimal.append(14)
            elif (DC_code_array[block_number][3:7] == '1111'): DC_decimal.append(15)
        elif (DC_code_array[block_number][0:3] == '110'):
            if   (DC_code_array[block_number][3:8] == '00000'): DC_decimal.append(-31)
            elif (DC_code_array[block_number][3:8] == '00001'): DC_decimal.append(-30)
            elif (DC_code_array[block_number][3:8] == '00010'): DC_decimal.append(-29)
            elif (DC_code_array[block_number][3:8] == '00011'): DC_decimal.append(-28)
            elif (DC_code_array[block_number][3:8] == '00100'): DC_decimal.append(-27)
            elif (DC_code_array[block_number][3:8] == '00101'): DC_decimal.append(-26)
            elif (DC_code_array[block_number][3:8] == '00110'): DC_decimal.append(-25)
            elif (DC_code_array[block_number][3:8] == '00111'): DC_decimal.append(-24)
            elif (DC_code_array[block_number][3:8] == '01000'): DC_decimal.append(-23)
            elif (DC_code_array[block_number][3:8] == '01001'): DC_decimal.append(-22)
            elif (DC_code_array[block_number][3:8] == '01010'): DC_decimal.append(-21)
            elif (DC_code_array[block_number][3:8] == '01011'): DC_decimal.append(-20)
            elif (DC_code_array[block_number][3:8] == '01100'): DC_decimal.append(-19)
            elif (DC_code_array[block_number][3:8] == '01101'): DC_decimal.append(-18)
            elif (DC_code_array[block_number][3:8] == '01110'): DC_decimal.append(-17)
            elif (DC_code_array[block_number][3:8] == '01111'): DC_decimal.append(-16)
            elif (DC_code_array[block_number][3:8] == '10000'): DC_decimal.append(16)
            elif (DC_code_array[block_number][3:8] == '10001'): DC_decimal.append(17)
            elif (DC_code_array[block_number][3:8] == '10010'): DC_decimal.append(18)
            elif (DC_code_array[block_number][3:8] == '10011'): DC_decimal.append(19)
            elif (DC_code_array[block_number][3:8] == '10100'): DC_decimal.append(20)
            elif (DC_code_array[block_number][3:8] == '10101'): DC_decimal.append(21)
            elif (DC_code_array[block_number][3:8] == '10110'): DC_decimal.append(22)
            elif (DC_code_array[block_number][3:8] == '10111'): DC_decimal.append(23)
            elif (DC_code_array[block_number][3:8] == '11000'): DC_decimal.append(24)
            elif (DC_code_array[block_number][3:8] == '11001'): DC_decimal.append(25)
            elif (DC_code_array[block_number][3:8] == '11010'): DC_decimal.append(26)
            elif (DC_code_array[block_number][3:8] == '11011'): DC_decimal.append(27)
            elif (DC_code_array[block_number][3:8] == '11100'): DC_decimal.append(28)
            elif (DC_code_array[block_number][3:8] == '11101'): DC_decimal.append(29)
            elif (DC_code_array[block_number][3:8] == '11110'): DC_decimal.append(30)
            elif (DC_code_array[block_number][3:8] == '11111'): DC_decimal.append(31)
        elif (DC_code_array[block_number][0:4] == '1110'):
            if   (DC_code_array[block_number][4:10] == '000000'): DC_decimal.append(-63)
            elif (DC_code_array[block_number][4:10] == '000001'): DC_decimal.append(-62)
            elif (DC_code_array[block_number][4:10] == '000010'): DC_decimal.append(-61)
            elif (DC_code_array[block_number][4:10] == '000011'): DC_decimal.append(-60)
            elif (DC_code_array[block_number][4:10] == '000100'): DC_decimal.append(-59)
            elif (DC_code_array[block_number][4:10] == '000101'): DC_decimal.append(-58)
            elif (DC_code_array[block_number][4:10] == '000110'): DC_decimal.append(-57)
            elif (DC_code_array[block_number][4:10] == '000111'): DC_decimal.append(-56)
            elif (DC_code_array[block_number][4:10] == '001000'): DC_decimal.append(-55)
            elif (DC_code_array[block_number][4:10] == '001001'): DC_decimal.append(-54)
            elif (DC_code_array[block_number][4:10] == '001010'): DC_decimal.append(-53)
            elif (DC_code_array[block_number][4:10] == '001011'): DC_decimal.append(-52)
            elif (DC_code_array[block_number][4:10] == '001100'): DC_decimal.append(-51)
            elif (DC_code_array[block_number][4:10] == '001101'): DC_decimal.append(-50)
            elif (DC_code_array[block_number][4:10] == '001110'): DC_decimal.append(-49)
            elif (DC_code_array[block_number][4:10] == '001111'): DC_decimal.append(-48)
            elif (DC_code_array[block_number][4:10] == '010000'): DC_decimal.append(-47)
            elif (DC_code_array[block_number][4:10] == '010001'): DC_decimal.append(-46)
            elif (DC_code_array[block_number][4:10] == '010010'): DC_decimal.append(-45)
            elif (DC_code_array[block_number][4:10] == '010011'): DC_decimal.append(-44)
            elif (DC_code_array[block_number][4:10] == '010100'): DC_decimal.append(-43)
            elif (DC_code_array[block_number][4:10] == '010101'): DC_decimal.append(-42)
            elif (DC_code_array[block_number][4:10] == '010110'): DC_decimal.append(-41)
            elif (DC_code_array[block_number][4:10] == '010111'): DC_decimal.append(-40)
            elif (DC_code_array[block_number][4:10] == '011000'): DC_decimal.append(-39)
            elif (DC_code_array[block_number][4:10] == '011001'): DC_decimal.append(-38)
            elif (DC_code_array[block_number][4:10] == '011010'): DC_decimal.append(-37)
            elif (DC_code_array[block_number][4:10] == '011011'): DC_decimal.append(-36)
            elif (DC_code_array[block_number][4:10] == '011100'): DC_decimal.append(-35)
            elif (DC_code_array[block_number][4:10] == '011101'): DC_decimal.append(-34)
            elif (DC_code_array[block_number][4:10] == '011110'): DC_decimal.append(-33)
            elif (DC_code_array[block_number][4:10] == '011111'): DC_decimal.append(-32)
            elif (DC_code_array[block_number][4:10] == '100000'): DC_decimal.append(32)
            elif (DC_code_array[block_number][4:10] == '100001'): DC_decimal.append(33)
            elif (DC_code_array[block_number][4:10] == '100010'): DC_decimal.append(34)
            elif (DC_code_array[block_number][4:10] == '100011'): DC_decimal.append(35)
            elif (DC_code_array[block_number][4:10] == '100100'): DC_decimal.append(36)
            elif (DC_code_array[block_number][4:10] == '100101'): DC_decimal.append(37)
            elif (DC_code_array[block_number][4:10] == '100110'): DC_decimal.append(38)
            elif (DC_code_array[block_number][4:10] == '100111'): DC_decimal.append(39)
            elif (DC_code_array[block_number][4:10] == '101000'): DC_decimal.append(40)
            elif (DC_code_array[block_number][4:10] == '101001'): DC_decimal.append(41)
            elif (DC_code_array[block_number][4:10] == '101010'): DC_decimal.append(42)
            elif (DC_code_array[block_number][4:10] == '101011'): DC_decimal.append(43)
            elif (DC_code_array[block_number][4:10] == '101100'): DC_decimal.append(44)
            elif (DC_code_array[block_number][4:10] == '101101'): DC_decimal.append(45)
            elif (DC_code_array[block_number][4:10] == '101110'): DC_decimal.append(46)
            elif (DC_code_array[block_number][4:10] == '101111'): DC_decimal.append(47)
            elif (DC_code_array[block_number][4:10] == '110000'): DC_decimal.append(48)
            elif (DC_code_array[block_number][4:10] == '110001'): DC_decimal.append(49)
            elif (DC_code_array[block_number][4:10] == '110010'): DC_decimal.append(50)
            elif (DC_code_array[block_number][4:10] == '110011'): DC_decimal.append(51)
            elif (DC_code_array[block_number][4:10] == '110100'): DC_decimal.append(52)
            elif (DC_code_array[block_number][4:10] == '110101'): DC_decimal.append(53)
            elif (DC_code_array[block_number][4:10] == '110110'): DC_decimal.append(54)
            elif (DC_code_array[block_number][4:10] == '110111'): DC_decimal.append(55)
            elif (DC_code_array[block_number][4:10] == '111000'): DC_decimal.append(56)
            elif (DC_code_array[block_number][4:10] == '111001'): DC_decimal.append(57)
            elif (DC_code_array[block_number][4:10] == '111010'): DC_decimal.append(58)
            elif (DC_code_array[block_number][4:10] == '111011'): DC_decimal.append(59)
            elif (DC_code_array[block_number][4:10] == '111100'): DC_decimal.append(60)
            elif (DC_code_array[block_number][4:10] == '111101'): DC_decimal.append(61)
            elif (DC_code_array[block_number][4:10] == '111110'): DC_decimal.append(62)
            elif (DC_code_array[block_number][4:10] == '111111'): DC_decimal.append(63)
    return DC_decimal