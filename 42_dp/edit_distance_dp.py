# then try dp 状态转移表

a = 'abcabc'
b = 'a'
import  math
min_distance = math.inf

def f(a, b):  # i: index of a; j: index of b; current_distance
    row = len(a)
    column = len(b)

    states = [[math.inf] * column for _ in range(row)]

    # initialize the first item
    if a[0] == b[0]:
        states[0][0] = 0
    else:
        states[0][0] = 1

    # initialize the first row
    for j in range(0, column):
        if a[0] == b[j]:
            states[0][j] = j
        elif j != 0:
            states[0][j] = states[0][j-1] + 1
        else:
            states[0][j] = 1

    # initialize the first column
    for i in range(0, row):
        if a[i] == b[0]:
            states[i][0] = i
        elif i != 0:
            states[i][0] = states[i-1][0] + 1
        else:
            states[i][0] = 1

    # iterate to the next state using dp way
    for i in range(1, row):
        for j in range(1, column):
            if a[i] == b[j]:
                states[i][j] = min(states[i-1][j-1], states[i-1][j]+1, states[i][j-1]+1)
            else:
                states[i][j] = min(states[i-1][j-1], states[i-1][j], states[i][j-1]) + 1

    return states[-1][-1]

print(f(a, b))
