# then try dp   状态转移方程
import math
total = 100
min_num = math.inf

mem = [False] * (total + 1)

def min_num_of_cards(total):
    if mem[total]:
        return mem[total]

    if total <= 2:
        return total

    if total == 3:
        return 1

    if total == 4:
        return 2

    if total == 5:
        return 1

    x = min(min_num_of_cards(total-1), min_num_of_cards(total-3), min_num_of_cards(total-5)) + 1
    mem[total] = x
    return x

print(min_num_of_cards(total))