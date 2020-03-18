import math
matrix = [
    [5, 0, 0, 0, 0],
    [7, 8, 0, 0, 0],
    [2, 3, 4, 0, 0],
    [4, 9, 6, 1, 0],
    [2, 7, 9, 4, 5],
]


def shortest_way(matrix):
    row = len(matrix)
    column = len(matrix[0])

    solutions = [[math.inf] * column for _ in range(row)]

    # initialize the solutions
    solutions[0][0] = matrix[0][0]

    # iterate to the next level(node) using dp way
    for i in range(1, row):
        for j in range(0, i+1):
            if j == 0:      # 只能从上面的点传递过来
                solutions[i][j] = solutions[i-1][j] + matrix[i][j]
            if j == i:      # 只能从斜上方的点传递过来
                solutions[i][j] = solutions[i-1][j-1] + matrix[i][j]
            else:
                solutions[i][j] = min(solutions[i-1][j-1], solutions[i-1][j]) + matrix[i][j]

    # check the last row
    min_path = math.inf
    for path in solutions[-1]:
        if path < min_path:
            min_path = path

    print(min_path)

    return min_path

shortest_way(matrix)



