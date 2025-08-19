#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'poisonousPlants' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY p as parameter.
#

def poisonousPlants(p):
    mdays = 0
    while True:
        stackA = [p[0]]
        stackB = []
        for i in range(1, len(p)):
            if p[i] > p[i-1]: # left < 
                stackB.append(p[i])
            else:
                stackA.append(p[i])
        if not stackB:  # no one died → finished
            break
        p = stackA
        mdays += 1
    return mdays

            



if __name__ == '__main__':

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    print(str(result))
