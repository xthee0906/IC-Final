# ==================================================================
# Copyright (c) 2024 National Tsing Hua University EE dept.
# Author: Tsung-Han Hsieh
# Description: Checker Functions for Debugging
# ==================================================================

def checkvalue(file_path, addr):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        value = lines[addr]
        print(file_path[10:-4] +' in addr.'+ str(addr))
        print(value)

def checkblock(addr):
    with open('dataset/Golden/SRAM_DCT.dat', 'r') as file:
        lines = file.readlines()
        value = lines[addr]
        a = value.split(' ')
    with open('dataset/Golden/SRAM_YCbCr.dat', 'r') as file:
        lines = file.readlines()
        value = lines[addr]
        b = value.split(' ')
    with open('dataset/Golden/SRAM_RGB.dat', 'r') as file:
        lines = file.readlines()
        value = lines[addr]
        c = value.split(' ')
    with open('dataset/BlockChecker/block_check.txt', 'w') as file:
        file.write(f'SRAM_addr_'+ str(addr) + ':\n')
        if (addr % 3 == 0):
            file.write(f'R_blcok_addr_'+ str(addr//3) + ':\n')
        elif (addr % 3 == 1):
            file.write(f'G_blcok_addr_'+ str(addr//3) + ':\n')
        else:
            file.write(f'B_blcok_addr_'+ str(addr//3) + ':\n')
        for i in range(8):
            for j in range(8):
                file.write(f'{c[i*8 + j].rjust(4)} ')
            file.write('\n')
        if (addr % 3 == 0):
            file.write(f'Y_blcok_addr_'+ str(addr//3) + ':\n')
        elif (addr % 3 == 1):
            file.write(f'Cb_blcok_addr_'+ str(addr//3) + ':\n')
        else:
            file.write(f'Cr_blcok_addr_'+ str(addr//3) + ':\n')
        for i in range(8):
            for j in range(8):
                file.write(f'{b[i*8 + j].rjust(4)} ')
            file.write('\n')
        if (addr % 3 == 0):
            file.write(f'DCT_Y_blcok_addr_'+ str(addr//3) + ':\n')
        elif (addr % 3 == 1):
            file.write(f'DCT_Cb_blcok_addr_'+ str(addr//3) + ':\n')
        else:
            file.write(f'DCT_Cr_blcok_addr_'+ str(addr//3) + ':\n')
        for i in range(8):
            for j in range(8):
                file.write(f'{a[i*8 + j].rjust(4)} ')
            file.write('\n')

