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
    results.append(start)

    while my_stack:
        curr_top = my_stack[-1]     # 只是拿当前的top, 并没有pop

        one_unvisited_adj = find_one_unvisited_adj(curr_top, adjs, seen)
        # current node is exhausted
        if one_unvisited_adj is None:
            my_stack.pop(-1)
        else:
            my_stack.append(one_unvisited_adj)
            seen.add(one_unvisited_adj)
            results.append(one_unvisited_adj)

    return results

def find_one_unvisited_adj(curr_node, adjs, visited):
    for adj in adjs[curr_node]:
        if adj not in visited:
            return adj

    # None is found
    return None


results = dfs(0, adjs)
print(results)      # [0, 1, 2, 5, 4, 3, 6, 7] 和递归版本输出是一样的