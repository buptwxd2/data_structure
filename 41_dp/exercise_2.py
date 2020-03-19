# then try dp   状态转移表
import math
total = 100
min_num = math.inf

def min_num_of_card(w):
    states = [[0] * (w + 1) for _ in range(w+1)]   # row number is (w+1) at most

    # initialize the first row
    states[0][0] = 1

    # forward
    for i in range(1, w+1):
        for j in range(w+1):
            if states[i-1][j]:
                if j + 1 <= w:
                    states[i][j+1] = 1
                if j + 3 <= w:
                    states[i][j+3] = 1
                if j + 5 <= w:
                    states[i][j+5] = 1

    for row in range(w+1):
        if states[row][-1]:
            print(row)
            return row
    else:
        return -1

min_num_of_card(total)