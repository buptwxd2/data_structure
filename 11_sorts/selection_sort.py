def selection_sort(list_to_sort):
    n = len(list_to_sort)
    if n == 0 or n == 1:
        return list_to_sort

    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if list_to_sort[j] < list_to_sort[min_idx]:
                min_idx = j

        swap(i, min_idx, list_to_sort)

    print(list_to_sort)
    return list_to_sort


def swap(i, j, list_to_sort):
    if i == j:
        return

    tmp = list_to_sort[i]
    list_to_sort[i] = list_to_sort[j]
    list_to_sort[j] = tmp

    return

test_list = [1,2,3,4,5,6]
import random
test_list = [random.randint(1,1000) for _ in range(100)]
print(test_list)


selection_sort(test_list)
print(sorted(test_list) == test_list)