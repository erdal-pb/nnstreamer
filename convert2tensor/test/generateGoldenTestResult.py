#!/usr/bin/env python
# Copyright (C) 2018 Samsung Electronics
# License: Apache-2.0
#
# @file generateGoldenTestResult.py
# @brief Generate golden test results for test cases
# @author MyungJoo Ham <myungjoo.ham@samsung.com>

from __future__ import print_function

from struct import *

# Returns: (string, string_size, expected_size)
# If string_size < expected_size, you do not need to check the results offset >= string_size.
# string: binary string (b'\xff\x00....')
def genCase01_RGB():
    string = ""
    string_size = 0
    expected_size = 280 * 40 * 3
    for i in range (0, 26):
        # White
        string_size = string_size + 40
        for j in range (0, 40):
            string += pack('BBB', 255, 255, 255)
        # Yellow
        string_size = string_size + 40
        for j in range (0, 40):
            string += pack('BBB', 255, 255, 0)
        # Light Blue
        string_size = string_size + 40
        for j in range (0, 40):
            string += pack('BBB', 0, 255, 255)
        # Green
        string_size = string_size + 40
        for j in range (0, 40):
            string += pack('BBB', 0, 255, 0)
        # Purple
        string_size = string_size + 40
        for j in range (0, 40):
            string += pack('BBB', 255, 0, 255)
        # Red
        string_size = string_size + 40
        for j in range (0, 40):
            string += pack('BBB', 255, 0, 0)
        # Blue
        string_size = string_size + 40
        for j in range (0, 40):
            string += pack('BBB', 0, 0, 255)
    for i in range (26, 30):
        # Blue
        string_size = string_size + 40
        for j in range (0, 40):
            string += pack('BBB', 0, 0, 255)
        # Black
        string_size = string_size + 40
        for j in range (0, 40):
            string += pack('BBB', 0, 0, 0)
        # Purple
        string_size = string_size + 40
        for j in range (0, 40):
            string += pack('BBB', 255, 0, 255)
        # Black
        string_size = string_size + 40
        for j in range (0, 40):
            string += pack('BBB', 0, 0, 0)
        # Light Blue
        string_size = string_size + 40
        for j in range (0, 40):
            string += pack('BBB', 0, 255, 255)
        # Black
        string_size = string_size + 40
        for j in range (0, 40):
            string += pack('BBB', 0, 0, 0)
        # White
        string_size = string_size + 40
        for j in range (0, 40):
            string += pack('BBB', 255, 255, 255)
    for i in range (0, 46):
        # Dark Blue
        string_size = string_size + 46
        string += pack('BBB', 0, 0, 128)
    for i in range (46, 93):
        # White
        string_size = string_size + 47
        string += pack('BBB', 255, 255, 255)
    for i in range (93, 140):
        # Gray Blue
        string_size = string_size + 47
        string += pack('BBB', 0, 128, 255)
    for i in range (140, 186):
        # Black
        string_size = string_size + 46
        string += pack('BBB', 0, 0, 0)
    for i in range (186, 210):
        # Dark Gray
        string_size = string_size + 24
        string += pack('BBB', 19, 19, 19)
    # We do not check the reset pixels: they are randomly generated.
    string_size = string_size * 3
    return (string, string_size, expected_size)

def genCase01_BGRx():
    string = ""
    string_size = 0
    expected_size = 280 * 40 * 4
    for i in range (0, 26):
        # White
        string_size = string_size + 40
        for j in range (0, 40):
            string += pack('BBBB', 255, 255, 255, 255)
        # Yellow
        string_size = string_size + 40
        for j in range (0, 40):
            string += pack('BBBB', 0, 255, 255, 255)
        # Light Blue
        string_size = string_size + 40
        for j in range (0, 40):
            string += pack('BBBB', 255, 255, 0, 255)
        # Green
        string_size = string_size + 40
        for j in range (0, 40):
            string += pack('BBBB', 0, 255, 0, 255)
        # Purple
        string_size = string_size + 40
        for j in range (0, 40):
            string += pack('BBBB', 255, 0, 255, 255)
        # Red
        string_size = string_size + 40
        for j in range (0, 40):
            string += pack('BBBB', 0, 0, 255, 255)
        # Blue
        string_size = string_size + 40
        for j in range (0, 40):
            string += pack('BBBB', 255, 0, 0, 255)
    for i in range (26, 30):
        # Blue
        string_size = string_size + 40
        for j in range (0, 40):
            string += pack('BBBB', 255, 0, 0, 255)
        # Black
        string_size = string_size + 40
        for j in range (0, 40):
            string += pack('BBBB', 0, 0, 0, 255)
        # Purple
        string_size = string_size + 40
        for j in range (0, 40):
            string += pack('BBBB', 255, 0, 255, 255)
        # Black
        string_size = string_size + 40
        for j in range (0, 40):
            string += pack('BBBB', 0, 0, 0, 255)
        # Light Blue
        string_size = string_size + 40
        for j in range (0, 40):
            string += pack('BBBB', 255, 255, 0, 255)
        # Black
        string_size = string_size + 40
        for j in range (0, 40):
            string += pack('BBBB', 0, 0, 0, 255)
        # White
        string_size = string_size + 40
        for j in range (0, 40):
            string += pack('BBBB', 255, 255, 255, 255)
    for i in range (0, 46):
        # Dark Blue
        string_size = string_size + 46
        string += pack('BBBB', 128, 0, 0, 255)
    for i in range (46, 93):
        # White
        string_size = string_size + 47
        string += pack('BBBB', 255, 255, 255, 255)
    for i in range (93, 140):
        # Gray Blue
        string_size = string_size + 47
        string += pack('BBBB', 255, 128, 0, 255)
    for i in range (140, 186):
        # Black
        string_size = string_size + 46
        string += pack('BBBB', 0, 0, 0, 255)
    for i in range (186, 210):
        # Dark Gray
        string_size = string_size + 24
        string += pack('BBBB', 19, 19, 19, 255)
    # We do not check the reset pixels: they are randomly generated.
    string_size = string_size * 4
    return (string, string_size, expected_size)


def write(filename, string):
    newfile = open(filename, 'wb')
    newfile.write(string)

write('testcase01.rgb.golden', genCase01_RGB()[0])
write('testcase01.bgrx.golden', genCase01_BGRx()[0])

