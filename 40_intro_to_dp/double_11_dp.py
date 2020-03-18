# 用DP解决双十一问题

items = [2, 2, 4, 6, 3]
lowest = 200          # capacity


def double_11_dp(lowest, items):
    # define a matrix to store all the states, shape: num * (weight+1)
    n = len(items)
    weight = 3 * lowest + 1

    states = [[False] * weight for _ in range(n)]

    # initialize the first row for the first item(0-th item)
    states[0][0] = True
    if items[0] <= weight:
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
    for j in range(lowest, weight, 1):
        if states[len(items)-1][j] == True:
            break
    else:
        return       # no solutions

    for i in range(len(items)-1, 1, -1):
        if j - items[i] >= 0 and states[i-1][j-items[i]] == True:
            print("Bought: {}".format(items[i]))
            j = j - items[i]
        else:
            pass        # did not buy the i-th item
    # check the first row -> the first item, buy or not to buy
    if j != 0:
        print("Bought: {}".format(items[0]))

double_11_dp(lowest, items)

