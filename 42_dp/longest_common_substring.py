a = 'abc'
b = 'ac'

def lcs(a, b):
    row = len(a)
    column = len(b)

    states = [[0] * column for _ in range(row)]

    # initialize the first row
    for j in range(column):
        if a[0] == b[j]:
            states[0][j] = 1
        else:
            if j != 0:
                states[0][j] = states[0][j-1]
            else:
                states[0][j] = 0

    # initialize the first column
    for i in range(row):
        if a[i] == b[0]:
            states[i][0] = 1
        else:
            if i != 0:
                states[i][0] = states[i-1][0]
            else:
                states[i][0] = 0

    # iterate to the next state using dp way
    for i in range(1, row):
        for j in range(1, column):
            if a [i] == b[j]:
                states[i][j] = max(states[i-1][j], states[i][j-1], states[i-1][j-1]+1)
            else:
                states[i][j] = max(states[i-1][j-1], states[i-1][j], states[i][j-1])

    return states[-1][-1]

print(lcs(a,b))