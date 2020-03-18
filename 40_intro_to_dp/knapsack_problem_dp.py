# 用DP解决0-1背包问题

items = [2, 2, 4, 6, 3]
weight = 9          # capacity


def knapsack_dp(weight, items):
    # define a matrix to store all the states, shape: num * (weight+1)
    n = len(items)

    states = [[False] * (weight + 1) for _ in range(n)]

    # initialize the first row for the first item(0-th item)
    states[0][0] = True
    if items[0] < weight:
        states[0][items[0]] = True

    # iteration to the next item
    for i in range(1, n):
        for j in range(weight+1):
            if states[i-1][j]:
                # NOT add the i-th item
                states[i][j] = True
                # Add the i-th item
                if j + items[i] <= weight:
                    states[i][j+items[i]] = True

    # check the last line state: states[num-1]
    for i in range(weight, -1, -1):
        if states[len(items)-1][i]:
            print(i)
            return i

    return 0

knapsack_dp(weight, items)