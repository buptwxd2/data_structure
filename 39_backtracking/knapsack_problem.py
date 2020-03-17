items = [3, 2, 4, 5]
max_weight = 8          # capacity
total_num = len(items)

max_weight_to_store = 0
def knapsack_problem(i, current_weight):        # going to handle the i-th (starting from zero) item
    global max_weight_to_store
    if i == total_num or current_weight == max_weight:
        if current_weight > max_weight_to_store:
            max_weight_to_store = current_weight
        return

    # a series of decisions
    # NOT take the i-th item
    knapsack_problem(i+1, current_weight)
    if current_weight + items[i] <= max_weight:
        knapsack_problem(i+1, current_weight+items[i])

print(knapsack_problem(0, 0))
print(max_weight_to_store)