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
# def f1(arr):

# def f2(arr):


def dynamicArray(n, queries):
    # Write your code here
    arr = [[] for i in range(n)] # Here is the dynamic array part 
    last_ans_arr = []
    last_ans = 0
    for element in queries:
        if element[0] == 1:
            idx = element[1] ^ last_ans % n
            arr[idx].append(element[2])
            # print(idx, last_ans)
        elif element[0] == 2:
            idx = element[1] ^ last_ans % n
            last_ans = arr[idx][element[2] % len(arr[idx])]
            last_ans_arr.append(last_ans)
    print(last_ans_arr) 
    return last_ans_arr
            

if __name__ == '__main__':
    # fptr = open(OUTPUT_PATH, 'w')

    # first_multiple_input = input().rstrip().split()

    # n = int(first_multiple_input[0])

    # q = int(first_multiple_input[1])

    # queries = []

    # for _ in range(q):
    #     queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(2, [[1,0,5],[1,1,7],[1,0,3],[2,1,0],[2,1,1]])

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()

