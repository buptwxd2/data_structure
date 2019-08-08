# This is the quick sort
# And its core is the partition function

def partition(list_to_sort, start, end):
    pivot = list_to_sort[end]
    pvt_idx = start  # indicating the final index of pivot

    for i in range(start, end):  # [0, pvt_idx-1] is the list whose values less than pivot.和选择排序类似
        if list_to_sort[i] <= pivot:
            # swap list_to_sort[i] and list_to_sort[pvt_idx]
            swap(list_to_sort, i, pvt_idx)
            pvt_idx += 1

    swap(list_to_sort, pvt_idx, end)

    return pvt_idx


def swap(my_list, i, j):
    if i == j:
        return

    tmp = my_list[i]
    my_list[i] = my_list[j]
    my_list[j] = tmp

    return

def quick_sort(list_to_sort, start, end):
    # if start >= end:
    #     return

    if len(list_to_sort) == 0 or len(list_to_sort) == 1:
        return

    pvt_idx = partition(list_to_sort, start, end)
    quick_sort(list_to_sort, start, pvt_idx-1)  # slice is a copy
    quick_sort(list_to_sort, pvt_idx+1, end)    # slice is a copy


list_a = [6, 4, 5, 7, 3, 2, 10, 1]
quick_sort(list_a, 0, len(list_a)-1)
print(list_a)

