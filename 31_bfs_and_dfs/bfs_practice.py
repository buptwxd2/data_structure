# Practice BFS on 6/23/2020 again
from collections import deque


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


# search
def bfs(start, end, adjs):
    if start == end:
        return

    my_queue = deque()
    visited = []

    prev = [-1] * len(adjs)

    # initialize the queue
    my_queue.append(start)

    while my_queue:
        curr_node = my_queue.popleft()

        for adj_node in adjs[curr_node]:

            if adj_node not in visited:
                prev[adj_node] = curr_node
                my_queue.append(adj_node)

        visited.append(curr_node)






