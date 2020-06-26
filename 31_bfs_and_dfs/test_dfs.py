adjs = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4],
    4: [1, 3, 5, 6],
    5: [2, 4, 7],
    6: [4, 7],
    7: [5, 6]
}


def depth_first_traverse_v1(start, adjs):
    my_stack = []
    visited = []
    output = []

    # initialize
    my_stack.append(start)
    visited.append(start)

    while my_stack:
        curr_top = my_stack.pop()
        output.append(curr_top)

        for adj in adjs[curr_top]:
            if adj not in visited:
                my_stack.append(adj)
                visited.append(adj)

    return output


print(depth_first_traverse_v1(0, adjs))