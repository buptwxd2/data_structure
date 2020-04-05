def bubble_sort(list_to_sort):
    n = len(list_to_sort)
    if n == 0 or n == 1:
        return list_to_sort

    for i in range(n-1):
        no_swap = True
        for j in range(n-1-i):
            if list_to_sort[j] > list_to_sort[j+1]:
                swap(j, j+1, list_to_sort)
                no_swap = False
        if no_swap:
            break

    print(list_to_sort)
    return list_to_sort

def swap(i, j, my_list):
    tmp = my_list[i]
    my_list[i] = my_list[j]
    my_list[j] = tmp

    return

import random
test_list = [random.randint(1,1000) for _ in range(100)]
print(test_list)


bubble_sort(test_list)
print(sorted(test_list) == test_list)
