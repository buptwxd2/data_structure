def bubble_sort(list_to_sort):
    n = len(list_to_sort)

    if n == 0 or n == 1:
        return list_to_sort

    for i in range(n-1, 0, -1):
        no_move = True
        for j in range(0, i):
            if list_to_sort[j] > list_to_sort[j+1]:
                swap(j, j+1, list_to_sort)  # swap in place
                no_move = False

        if no_move:
            break   # 提前退出

    print(list_to_sort)
    return list_to_sort


def swap(i, j, my_list):
    tmp = my_list[i]
    my_list[i] = my_list[j]
    my_list[j] = tmp

    return

test_list = [6, 5, 4, 3, 2, 1]
bubble_sort(test_list)
