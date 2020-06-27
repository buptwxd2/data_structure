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


def bfs(start, adjs):
    my_queue = []
    seen = set()
    results = []

    # initialize
    my_queue.append(start)
    seen.add(start)

    while my_queue:
        node = my_queue.pop(0)
        results.append(node)

        for adj in adjs[node]:
            if adj not in seen:
                my_queue.append(adj)
                seen.add(adj)

    return results

results = bfs(0, adjs)
print(results)      #  [0, 1, 3, 2, 4, 5, 6, 7]