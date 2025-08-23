#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid
#  2. INTEGER startX
#  3. INTEGER startY
#  4. INTEGER goalX
#  5. INTEGER goalY
#

INF = 10**9

def minimumMoves(grid, startX, startY, goalX, goalY):
    n = len(grid)
    vis = [[False]*n for _ in grid]
    dist = [[INF]*n for _ in grid]
    
    # head is for queue
    q = []
    head = 0

    # initialize
    vis[startX][startY] = True
    dist[startX][startY] = 0
    q.append((startX, startY))

    while head < len(q):
        x, y = q[head]
        head += 1
        d = dist[x][y]
        if (x, y) == (goalX, goalY):
            return d
        # go up
        nx = x - 1
        while nx >= 0 and grid[nx][y] == '.': # 如果沒有超出大小、grid 也不是 'X'
            if not vis[nx][y]: # 沒有訪問過
                vis[nx][y] = True
                dist[nx][y] = d + 1
                q.append((nx, y))
            nx -= 1
        # go down
        nx = x + 1
        while nx < n and grid[nx][y] == '.':
            if not vis[nx][y]:
                vis[nx][y] = True
                dist[nx][y] = d + 1
                q.append((nx, y))
            nx += 1
        
        # go right
        ny = y + 1
        while ny < n and grid[x][ny] == '.':
            if not vis[x][ny]:
                vis[x][ny] = True
                dist[x][ny] = d + 1
                q.append((x, ny))
            ny += 1
        
        # go left
        ny = y - 1
        while ny >= 0 and grid[x][ny] == '.':
            if not vis[x][ny]:
                vis[x][ny] = True
                dist[x][ny] = d + 1
                q.append((x, ny))
            ny -= 1
    return -1

if __name__ == '__main__':

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    first_multiple_input = input().rstrip().split()

    startX = int(first_multiple_input[0])

    startY = int(first_multiple_input[1])

    goalX = int(first_multiple_input[2])

    goalY = int(first_multiple_input[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)
    print(result)