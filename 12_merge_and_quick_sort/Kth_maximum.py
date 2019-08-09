# Using O(n) to find the Kth maximum value of an array, refer to quick sort


def find_kth_max(list_to_sort, start, end, k):
    if k > end + 1:
        return None

    # input a list, and it's staring with (start) and ending with (end)
    # After partition, the pivot index is p_idx
    # So there are (p_idx-start) elements before the pivot in the sub list
    # if k is larger than (p_idx-start)+1(including pivot), we need to look for the [k-(p_idx-start+1)]th max in the rear sub-list
    p_idx = partition(list_to_sort, start, end)
    if p_idx - start + 1 == k:
        return list_to_sort[p_idx]
    elif p_idx - start + 1 < k:
        return find_kth_max(list_to_sort, p_idx + 1, end, k-(p_idx-start+1))
    elif p_idx - start + 1 > k:
        return find_kth_max(list_to_sort, start, p_idx - 1, k)


def partition(list_to_sort, start, end):
    pivot = list_to_sort[end]
    p_idx = start

    for i in range(start, end):
        if list_to_sort[i] <= pivot:
            swap(list_to_sort, i, p_idx)
            p_idx += 1

    swap(list_to_sort, p_idx, end)

    return p_idx

def swap(list_to_swap, i, j):
    if i == j:
        return

    tmp = list_to_swap[i]
    list_to_swap[i] = list_to_swap[j]
    list_to_swap[j] = tmp

    return


list_a = [7, 10, 4, 3, 20, 15]
# print(find_kth_max(list_a, 0, 5, 5))
# print(list_a)

for i in range(len(list_a)):
    my_list = list(list_a)
    print(find_kth_max(my_list, 0, 5, i+1))
    print(my_list)
