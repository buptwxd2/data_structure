from collections import deque

# assume we already built an adjacent matrix called adj[][]
# adj = {
#     1: [2, 3],
#     2: [1, 4, 5],
#     3: [1, 6, 7],
#     4: [2],
#     5: [2],
#     6: [3],
#     7: [3]
# }

adj = {
    1: [2, 4],
    2: [1, 3, 5, 7, 8],
    3: [2, 4, 9, 10],
    4: [1, 3],
    5: [2, 6, 7, 8],
    6: [5],
    7: [2,5,8],
    8: [2,5,7],
    9: [3],
    10: [3]
}

def bfs(start):
    visited = [False] * (len(adj) + 1)   # total number of nodes, starting from 1, instead of 0

    # use queue to implement bfs algorithm
    my_queue = deque()
    prev = []

    my_queue.append(start)

    while my_queue:
        current_node = my_queue.popleft()
        visited[current_node] = True
        prev.append(current_node)

        curr_node_adjs = adj[current_node]

        for adj_node in curr_node_adjs:
            if not visited[adj_node]:
                if adj_node not in my_queue:
                    my_queue.append(adj_node)

    print("->".join(str(x) for x in prev))
    return prev

bfs(1)



