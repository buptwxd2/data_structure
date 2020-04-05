def insertion_sort(list_to_sort):
    n = len(list_to_sort)

    if n == 0 or n == 1:
        return list_to_sort

    for i in range(1, n):
        for j in range(i):
            # from left to right to find the correct place to insert
            # see insertion_sort_2 to scan from right to left
            if list_to_sort[i] < list_to_sort[j]:
                tmp = list_to_sort[i]

                for k in range(i, j, -1):
                    list_to_sort[k] = list_to_sort[k-1]

                list_to_sort[j] = tmp
                break

    print(list_to_sort)
    return list_to_sort


def insertion_sort_2(list_to_sort):
    n = len(list_to_sort)

    if n == 0 or n == 1:
        return list_to_sort

    for i in range(1, n):
        tmp = list_to_sort[i]
        for j in range(i-1, -1, -1):
            # from right to left to find the correct place to insert
            if tmp < list_to_sort[j]:
                list_to_sort[j+1] = list_to_sort[j]
            else:
                list_to_sort[j+1] = tmp
                break

    print(list_to_sort)
    return list_to_sort

import random
test_list = [random.randint(1,1000) for _ in range(100)]
# test_list = [1,2,3,4,5,6]
print(test_list)


insertion_sort_2(test_list)
print(sorted(test_list) == test_list)
