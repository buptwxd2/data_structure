def quick_sort(list_to_sort, low, high):
    if low >= high:
        return

    pivot_idx = partition(list_to_sort, low, high)
    quick_sort(list_to_sort, low, pivot_idx-1)
    quick_sort(list_to_sort, pivot_idx+1, high)



# https://en.wikipedia.org/wiki/Quicksort Lomuto partition scheme
# def partition(list_to_sort, low, high):
#     pivot = list_to_sort[high]
#     pivot_idx = low
#
#     for i in range(low, high):
#         if list_to_sort[i] < pivot:
#             swap(list_to_sort, i, pivot_idx)
#             pivot_idx += 1
#
#     swap(list_to_sort, pivot_idx, high)
#
#     print(list_to_sort)
#     print(pivot_idx)
#
#     return pivot_idx

# https://en.wikipedia.org/wiki/Quicksort Hoare partition scheme
def partition(list_to_sort, low, high):
    pivot = list_to_sort[low]
    high = high

    while low < high:
        while low < high and list_to_sort[high] >= pivot:
            high -= 1
        swap(list_to_sort, high, low)

        while low < high and list_to_sort[low] < pivot:
            low += 1
        swap(list_to_sort, low, high)

    # print(list_to_sort)
    return low

def swap(my_list, i, j):
    tmp = my_list[i]
    my_list[i] = my_list[j]
    my_list[j] = tmp

    return

test_list = [5,6,3,2,4]
# partition(test_list, 0, 4)
quick_sort(test_list, 0, 4)
print(test_list)