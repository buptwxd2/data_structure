# 用DP解决0-1背包问题

capacity = 9            # capacity
weights = [2, 2, 4, 6, 3]
values = [3, 4, 8, 9, 6]


def knapsack_dp(capacity, weights, values):
    # define a matrix to store all the states, shape: num * (capacity+1)
    n = len(weights)

    states = [[-1] * (capacity + 1) for _ in range(n)]

    # initialize the first row for the first item(0-th item)
    states[0][0] = 0
    if weights[0] <= capacity:
        states[0][weights[0]] = values[0]

    # iteration to the next item
    for i in range(1, n):
        for j in range(capacity + 1):
            # NOT add the i-th item
            if states[i-1][j] > states[i][j]:
                states[i][j] = states[i-1][j]
            # Add the i-th item
            if j + weights[i] <= capacity:
                if states[i-1][j] + values[i] > states[i][j+weights[i]]:
                    states[i][j+weights[i]] = states[i-1][j] + values[i]

    # check the last line state: states[num-1]
    max_value = -1
    for value in states[-1]:
        if value > max_value:
            max_value = value

    print(max_value)
    return max_value

knapsack_dp(capacity, weights, values)