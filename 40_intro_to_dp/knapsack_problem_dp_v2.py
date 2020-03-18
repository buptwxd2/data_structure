# 用DP解决0-1背包问题
# v2: 降低空间复杂度，states reduce from n * w to w

items = [2, 2, 4, 6, 3]
weight = 9          # capacity


def knapsack_dp(weight, items):
    # define a matrix to store all the states, shape: num * (weight+1)
    n = len(items)

    states = [[False] * (weight + 1) for _ in range(n)]
    states = [False] * (weight + 1)

    # initialize the first row for the first item(0-th item)
    states[0] = True
    if items[0] <= weight:
        states[items[0]] = True

    # iteration to the next item, this is the dp process
    for i in range(1, n):
        for j in range(weight, -1, -1):
            if states[j]:
                if j + items[i] <= weight:
                    states[j+items[i]] = True

    # check the last line state: states[num-1]
    for i in range(weight, -1, -1):
        if states[i]:
            print(i)
            return i

    return 0

knapsack_dp(weight, items)