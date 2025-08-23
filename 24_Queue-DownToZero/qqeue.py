#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque
#
# Complete the 'downToZero' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def downToZero(n):
    # Write your code here
    visited = [False] * (n+1)
    q = deque() 
    q.append((n, 0))

    while q:
        x, step = q.popleft()
        print(x, step)

        if x == 0:
            return step
        
        if not visited[x-1]:
            visited[x-1] = True
            q.append((x-1, step + 1))
            
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                nxt = max(i, x//i)
                if not visited[nxt]:
                    visited[nxt] = True
                    q.append((nxt, step+1))

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = downToZero(n)
        print(result)