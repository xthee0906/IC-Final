# ==================================================================
# Copyright (c) 2024 National Tsing Hua University EE dept.
# Author: Tsung-Han Hsieh
# Description: Functions for Checking Value for Debugging
# ==================================================================

def get_RGB_value_forcheck(image):
    c = 0
    a = 0
    B_channel_values = image[:, :, 0] # B
    G_channel_values = image[:, :, 1] # G
    R_channel_values = image[:, :, 2] # R
    output_file_path = './dataset/ChannelValue/RGB/R_channel_values.txt'
    with open(output_file_path, 'w') as file:
        for row in R_channel_values:
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

    output_file_path = './dataset/ChannelValue/RGB/G_channel_values.txt'
    with open(output_file_path, 'w') as file:
        for row in G_channel_values:
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


    output_file_path = './dataset/ChannelValue/RGB/B_channel_values.txt'
    with open(output_file_path, 'w') as file:
        for row in B_channel_values:
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

def get_YCbCr_value_forcheck(image):
    c = 0
    a = 0
    Y_channel_values = image[:, :, 0] # Y
    Cb_channel_values = image[:, :, 2] # Cb
    Cr_channel_values = image[:, :, 1] # Cr
    output_file_path = './dataset/ChannelValue/YCbCr/Y_channel_values.txt'
    with open(output_file_path, 'w') as file:
        for row in Y_channel_values:
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


    output_file_path = './dataset/ChannelValue/YCbCr/Cb_channel_values.txt'
    with open(output_file_path, 'w') as file:
        for row in Cb_channel_values:
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


    output_file_path = './dataset/ChannelValue/YCbCr/Cr_channel_values.txt'
    with open(output_file_path, 'w') as file:
        for row in Cr_channel_values:
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

def get_DCT_value_forcheck(image):
    c = 0
    a = 0
    Y_channel_values = image[:, :, 0]  # Y
    Cb_channel_values = image[:, :, 2] # Cb
    Cr_channel_values = image[:, :, 1] # Cr
    output_file_path = './dataset/ChannelValue/DCT/DCT_channel_Y_values.txt'
    with open(output_file_path, 'w') as file:
        for row in Y_channel_values:
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


    output_file_path = './dataset/ChannelValue/DCT/DCT_channel_Cb_values.txt'
    with open(output_file_path, 'w') as file:
        for row in Cb_channel_values:
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

    output_file_path = './dataset/ChannelValue/DCT/DCT_channel_Cr_values.txt'
    with open(output_file_path, 'w') as file:
        for row in Cr_channel_values:
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

def get_Q_value_forcheck(image):
    c = 0
    a = 0
    Y_channel_values = image[:, :, 0]  # Y
    Cb_channel_values = image[:, :, 2] # Cb
    Cr_channel_values = image[:, :, 1] # Cr
    output_file_path = './dataset/ChannelValue/Q/Q_channel_Y_values.txt'
    with open(output_file_path, 'w') as file:
        for row in Y_channel_values:
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


    output_file_path = './dataset/ChannelValue/Q/Q_channel_Cb_values.txt'
    with open(output_file_path, 'w') as file:
        for row in Cb_channel_values:
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

    output_file_path = './dataset/ChannelValue/Q/Q_channel_Cr_values.txt'
    with open(output_file_path, 'w') as file:
        for row in Cr_channel_values:
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
