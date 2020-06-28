

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

# recursive dfs; 其实就是回溯法（？有点区别是回溯做了选择退回来后会清掉之前的选择，但是这里seen并没有清掉而且还不能清掉）
results = []
def recur_dfs(start, adjs, seen):
    results.append(start)
    seen.add(start)

    for adj in adjs[start]:
        if adj not in seen:
            recur_dfs(adj, adjs, seen)

recur_dfs(0, adjs, set())
print(results)  # [0, 1, 2, 5, 4, 3, 6, 7]