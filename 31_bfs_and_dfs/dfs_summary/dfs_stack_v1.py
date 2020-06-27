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

def dfs(start, adjs):
    my_stack = []
    seen = set()
    results = []

    # initialize
    my_stack.append(start)
    seen.add(start)

    while my_stack:
        curr_top = my_stack.pop(-1)
        results.append(curr_top)

        for adj in adjs[curr_top]:
            if adj not in seen:
                my_stack.append(adj)
                seen.add(adj)

    return results

results = dfs(0, adjs)
print(results)      #   [0, 3, 4, 6, 7, 5, 2, 1]