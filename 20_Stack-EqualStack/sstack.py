#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def equalStacks1(h1, h2, h3):
    # Write your code here
    while sum(h1) != sum(h2) and sum(h2) != sum(h3):
        if sum(h1) >= sum(h2) and sum(h1) >= sum(h3):
            h1.pop(0)
        elif sum(h2) >= sum(h1) and sum(h2) >= sum(h3):
            h2.pop(0)
        else:
            h3.pop(0)
    return sum(h1)

def equalStacks(h1, h2, h3):
    # Write your code here
    s1, s2, s3 = sum(h1), sum(h2), sum(h3)
    i, j, k = 0, 0, 0
    while True:
        if i == len(h1) or j == len(h2) or k == len(h3):
            return 0
        
        if s1 == s2 and s2 == s3:
            return s1
        
        if s1 >= s2 and s1 >= s3:
            s1 -= h1[i]
            i += 1
        elif s2 >= s1 and s2 >= s3:
            s2 -= h2[j]
            j += 1
        else:
            s3 -= h3[k]
            k += 1

if __name__ == '__main__':
    

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)
    print(result)
    
    