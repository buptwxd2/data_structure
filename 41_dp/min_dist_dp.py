# 状态转移表法

matrix = [
    [1,3,5,9],
    [2,1,3,4],
    [5,2,6,7],
    [6,8,4,3],
]

import math

def min_dist_dp(matrix):
    row = len(matrix)
    column = len(matrix[0])

    #状态转移表中的表，用来存储到(i,j)的最短距离
    states = [[math.inf] * column for _ in range(row)]

    # initialize the table/states
    # first row
    for j in range(column):
        states[0][j] = sum(matrix[0][:j+1])

    # first column
    for i in range(row):
        states[i][0] = sum(x[0] for x in matrix[:i+1])

    # iterate to the next state using dp way
    for i in range(1, row):
        for j in range(1, column):
            states[i][j] = min(states[i][j-1], states[i-1][j]) + matrix[i][j]

    print(states)

    return states[-1][-1]

min_dist_dp(matrix)