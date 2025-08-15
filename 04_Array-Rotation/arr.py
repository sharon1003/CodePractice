#!/bin/python3

import math
import os
import random
import re
import sys

OUTPUT_PATH = '/Users/pengwenhsuan/Desktop/GitHub/CodePractice/02_Array-2DS/test.txt'
#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#


def rotateLeft(d, arr):
    # Write your code here
    temp_arr = [ 0 for i in range(n)]
    for old_index in range(n):
        new_position = old_index - d
        if new_position < 0:
            new_position = new_position + n
        temp_arr[new_position] = arr[old_index]
    return temp_arr
if __name__ == '__main__':

    n = 5

    result = rotateLeft(4, [1, 2, 3, 4, 5])

