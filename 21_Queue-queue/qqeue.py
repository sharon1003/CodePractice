# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import os
import random
import re
import sys
from collections import deque

def queue(operations):
    return_stack = []
    dq = deque()
    for ops in operations:
        op = int(ops.split(' ')[0])
        if op == 1:  # enqueue
            num = int(ops.split(' ')[1])
            dq.append(num)
        elif op == 2:  # dequeue
            dq.popleft()
        elif op == 3:  # print front
            return_stack.append(dq[0])
    return return_stack

def queue(operations):
    return_stack = []
    stack = []
    for ops in operations:
        op = int(ops.split(' ')[0])
        if op == 1:
            num = (int(ops.split(' ')[1]))
            stack.append(num)
        elif op == 2:
            stack.pop(0)
        elif op == 3:
            return_stack.append(stack[0])
    return return_stack

if __name__ == '__main__':
    q = int(input())
    ops = []
    for _ in range(q):
        ops_item = input().strip()
        ops.append(ops_item)
    result = queue(ops)
    print(result)
