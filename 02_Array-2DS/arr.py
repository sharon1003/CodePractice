#!/bin/python3

import math
import os
import random
import re
import sys
OUTPUT_PATH = '/Users/pengwenhsuan/Desktop/GitHub/CodePractice/02_Array-2DS/test.txt'

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
def cal(arr):
    # input 3*3
    # [1, 1, 1]
    # [1, 1, 1]
    # [1, 1, 1]
    # output = 7
    return sum(arr[0]) + arr[1][1] + sum(arr[2])


def hourglassSum(arr):
    temp_max = -float('inf') # little tips
    for row in range(4):
        for col in range(4):
            f = cal([arr[row][col:col+3], arr[row+1][col:col+3], arr[row+2][col:col+3]])
            if f > temp_max:
                temp_max = f
    return temp_max

if __name__ == '__main__':
    fptr = open(OUTPUT_PATH, 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
