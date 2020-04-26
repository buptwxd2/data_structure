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


def depth_first_traverse(start, adjs):
    my_stack = []

    visited = []

    # initialize
    my_stack.append(start)

    while my_stack:
        curr_top = my_stack.pop()

        if curr_top not in visited:
            visited.append(curr_top)

            for adj in adjs[curr_top]:
                if adj not in visited:
                    my_stack.append(adj)

    return visited

print(depth_first_traverse(0, adjs))


def depth_first_traverse_v2(start, adjs):
    my_stack = []

    visited = []

    # initialize
    my_stack.append(start)

    while my_stack:
        curr_top = my_stack[-1]
        if curr_top not in visited:
            visited.append(curr_top)

        one_unvisited_adj = find_one_unvisited_adj(curr_top, adjs, visited)
        # current node is exhausted
        if one_unvisited_adj is None:
            my_stack.pop(-1)
        else:
            my_stack.append(one_unvisited_adj)

    return visited

def find_one_unvisited_adj(curr_node, adjs, visited):
    for adj in adjs[curr_node]:
        if adj not in visited:
            return adj

    # None is found
    return None

print(depth_first_traverse_v2(0, adjs))

"""
Reference
depth_first_traverse:
https://en.wikipedia.org/wiki/Depth-first_search Pseudocode Section

depth_first_traverse_v2 :
Algorithm: https://www.tutorialspoint.com/data_structures_algorithms/depth_first_traversal.htm
            https://www.youtube.com/watch?v=pcKY4hjDrxk
Code:       https://www.tutorialspoint.com/data_structures_algorithms/depth_first_traversal_in_c.htm
"""


