#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    stack = []
    for i in s:
        if i == '{': 
            stack.append('}')
        elif i == '(':
            stack.append(')')
        elif i == '[':
            stack.append(']')
        else:
            if stack.pop() != i:
                return 'No'
    return 'YES'
                

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)
    print(result)
