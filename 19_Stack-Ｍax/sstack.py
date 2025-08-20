#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def getMax(operations):
    # Write your code here
    stack = []
    max_stack = []
    stack_return = []
    for op in operations:
        operation = op.split(' ')[0]
        if operation == str(1):
            num = int(op.split(' ')[1])
            stack.append(num)
            if not max_stack:
                max_stack.append(num)
            else:
                max_stack.append(max(max_stack[-1], num))
        elif operation == str(2):
            stack.pop()
            max_stack.pop()
        elif operation == str(3):
            # Can not use this one becuase it cost extra time
            stack_return.append(max_stack[-1])
    print(max_stack)
    return stack_return

if __name__ == '__main__':

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)


