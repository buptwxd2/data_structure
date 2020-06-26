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


def breadth_first_traverse(start, adjs):
    queue = deque()      # queue 是一个队列，用来存储已经被访问、但相连的顶点还没有被访问的顶点
    visited = []         # 存储当前已经访问过的节点
    output  = []        # bfs结果输出，遍历顺序

    # initialize for the first vertex: start
    visited.append(start)
    queue.append(start)

    while queue:
        vertex_to_handle = queue.popleft()
        output.append(vertex_to_handle)

        adj_nodes = adjs[vertex_to_handle]
        for adj_node in adj_nodes:
            if adj_node not in visited:
                visited.append(adj_node)
                queue.append(adj_node)

    return visited

print(" ".join(str(node) for node in breadth_first_traverse(0, adjs)))