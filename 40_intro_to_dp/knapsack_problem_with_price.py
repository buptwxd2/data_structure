# 用memory + 回溯来解决0-1背包问题

items = [2, 2, 4, 6, 3]
values = [3, 4, 8, 9, 6]
max_weight = 9          # capacity
total_num = len(items)

max_weight_to_store = 0
max_value = 0


def knapsack_problem(i, current_weight, current_value):        # going to handle the i-th (starting from zero) item
    global max_weight_to_store
    global max_value

    if i == total_num or current_weight == max_weight:
        if current_value > max_value:
            max_value = current_value
        return

    # a series of decisions
    # NOT take the i-th item
    knapsack_problem(i+1, current_weight, current_value)
    if current_weight + items[i] <= max_weight:
        knapsack_problem(i+1, current_weight+items[i], current_value + values[i])

print(knapsack_problem(0, 0,0))
print(max_value)