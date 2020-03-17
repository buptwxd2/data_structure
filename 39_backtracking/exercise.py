items = [3, 2, 4, 5]
prices = [100, 1, 1, 1]
max_weight = 8          # capacity
total_num = len(items)

# max price after making the choice
max_price = 0
# final choices
choices = [0] * len(items)

def knapsack_problem(i, current_weight):        # going to handle the i-th (starting from zero) item
    global max_price

    if i == total_num or current_weight == max_weight:
        print("Choices: {}".format(choices))
        price = cal_final_price(prices, choices)
        print("Price: {}".format(price))

        if price > max_price:
            max_price = price
        return

    # a series of decisions
    # NOT take the i-th item
    choices[i] = 0
    knapsack_problem(i+1, current_weight)
    if current_weight + items[i] <= max_weight:
        choices[i] = 1
        knapsack_problem(i+1, current_weight+items[i])

def cal_final_price(prices, choices):
    return sum(p * c for p,c in zip(prices, choices))

print(knapsack_problem(0, 0))
print(max_price)
