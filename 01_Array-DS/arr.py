#!/bin/python3

import math
import os
import random
import re
import sys
OUTPUT_PATH = '/Users/pengwenhsuan/Desktop/GitHub/CodePractice/01_Array-DS/test.txt'
#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def reverseArray1(a):    
    temp_arr = a.copy()
    for index, num in enumerate(a):
        temp_i = len(a) - 1 - int(index)
        temp_arr[temp_i] = num
    return temp_arr

def reverseArray2(a):
    left = 0
    right = len(a) - 1
    while left < right:
        a[left], a[right] = a[right], a[left]
        left += 1
        right -= 1
    return a
        

if __name__ == '__main__':
    fptr = open(OUTPUT_PATH, 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray2(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
