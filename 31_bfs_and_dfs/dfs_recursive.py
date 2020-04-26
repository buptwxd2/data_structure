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

# this graph comes from 极客时间#31讲中的BFS中的图

found = False


def dfs(start, end, adjs):
    global found

    v = len(adjs)

    visited = [False] * v
    prev = [-1] * v

    recur_dfs(start, end, visited, prev)
    my_print(prev, start, end)


def recur_dfs(start, end, visited, prev):
    global found
    if found:
        return

    visited[start] = True
    if start == end:
        found = True
        return

    for adj in adjs[start]:
        if not visited[adj]:
            prev[adj] = start
            recur_dfs(adj, end, visited, prev)


def my_print(prev, start, end):
    if start == end:
        print(end)
        return
    else:
        my_print(prev, start, prev[end])
        print(end)

dfs(0, 6, adjs)



def depth_first_traverse_recursive(start, adjs, visited):
    visited += [start]

    for adj in adjs[start]:
        if adj not in visited:
            depth_first_traverse_recursive(adj, adjs, visited)

    return visited

print(depth_first_traverse_recursive(0, adjs, []))