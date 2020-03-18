# 用memory + 回溯来解决0-1背包问题

items = [2, 2, 4, 6, 3]
max_weight = 9          # capacity
total_num = len(items)

max_weight_to_store = 0
# add memory
mem = [False] * total_num
mem = [mem for _ in range(max_weight)]

def knapsack_problem(i, current_weight):        # going to handle the i-th (starting from zero) item
    global max_weight_to_store
    if i == total_num or current_weight == max_weight:
        if current_weight > max_weight_to_store:
            max_weight_to_store = current_weight
        return

    # before calculating, check if is calculated
    if mem[i][current_weight]:
        return

    mem[i][current_weight] = True
    # a series of decisions
    # NOT take the i-th item
    knapsack_problem(i+1, current_weight)
    if current_weight + items[i] <= max_weight:
        knapsack_problem(i+1, current_weight+items[i])

print(knapsack_problem(0, 0))
print(max_weight_to_store)