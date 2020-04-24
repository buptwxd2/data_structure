# Re-implement bfs in 2020
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

def bfs(start, end, adjs):
    if start == end:
        return

    v = len(adjs)    # v is the number of the vertex

    queue = deque()      # queue 是一个队列，用来存储已经被访问、但相连的顶点还没有被访问的顶点
    visited = [False] * v
    prev = [-1] * v

    # initialize for the first vertex: start
    visited[start] = True
    queue.append(start)

    while queue:
        vertex_to_handle = queue.popleft()
        for adj_node in adjs[vertex_to_handle]:
            if not visited[adj_node]:
                prev[adj_node] = vertex_to_handle
                visited[adj_node] = True
                queue.append(adj_node)

                if adj_node == end:
                    my_print(prev, start, end)
                    return


def my_print(prev, start, end):
    if start == end:
        print(end)
        return
    else:
        my_print(prev, start, prev[end])
        print(end)

bfs(0, 7, adjs)


def breadth_first_traverse(start, adjs):
    queue = deque()      # queue 是一个队列，用来存储已经被访问、但相连的顶点还没有被访问的顶点
    visited = []         # 存储当前已经访问过的节点

    # initialize for the first vertex: start
    visited.append(start)
    queue.append(start)

    while queue:
        vertex_to_handle = queue.popleft()

        adj_nodes = adjs[vertex_to_handle]
        for adj_node in adj_nodes:
            if adj_node not in visited:
                visited.append(adj_node)
                queue.append(adj_node)

    return visited


visited = breadth_first_traverse(0, adjs)
print(" ".join(str(node) for node in visited))

