# This is the quick sort
# And its core is the partition function

def partition(list_to_sort):
    start = 0
    end = len(list_to_sort) - 1
    pivot = list_to_sort[end]
    pvt_idx = start  # indicating the final index of pivot

    for i in range(start, end):  # i indicating the index whose value less than pivot
        if list_to_sort[i] <= pivot:
            # swap list_to_sort[i] and list_to_sort[pvt_idx]
            tmp = list_to_sort[i]
            list_to_sort[i] = list_to_sort[pvt_idx]
            list_to_sort[pvt_idx] = tmp
            pvt_idx += 1

    return pvt_idx

def quick_sort(list_to_sort):
    if len(list_to_sort) == 0 or len(list_to_sort) == 1:
        return

    pvt_idx = partition(list_to_sort)
    quick_sort(list_to_sort[0:pvt_idx-1])
    quick_sort(list_to_sort[pvt_idx+1:])

list_a = [6, 4, 5, 7, 3, 2, 10, 1]
quick_sort(list_a)
print(list_a)