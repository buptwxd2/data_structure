# 状态转移方程法

matrix = [
    [1,3,5,9],
    [2,1,3,4],
    [5,2,6,7],
    [6,8,4,3],
]

import math
row = len(matrix)
column = len(matrix[0])

mem = [[math.inf] * column for _ in range(row)]

def min_dist(i, j):
    global mem

    if mem[i][j] != math.inf:
        return mem[i][j]

    if i == 0:
        dist = sum(matrix[0][:j+1])
        mem[i][j] = dist
        return dist

    if j == 0:
        dist = sum(row[0] for row in matrix[:i+1])
        return dist

    dist = min(min_dist(i-1, j), min_dist(i, j-1)) + matrix[i][j]
    return dist

print(min_dist(3,3))