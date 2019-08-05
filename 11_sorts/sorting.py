"""
Three traditional sorting algorithms: bubble/insertion/selection
"""


# bubble sorting
# Ascending: 小 -> 大
def bubble_sort(sorting_list):
    length = len(sorting_list)

    for i in range(length):
        flag = True
        for j in range(length-i-1):
            if sorting_list[j] > sorting_list[j+1]:
                tmp = sorting_list[j]
                sorting_list[j] = sorting_list[j+1]
                sorting_list[j+1] = tmp
                flag = False
        if flag:
            break


# insertion sort
# Ascending way
def insertion_sort(sorting_list):
    length = len(sorting_list)
    for i in range(length - 1):
        # try insert (i+1) element to the [0, 1, ... i] list
        next_value = sorting_list[i+1]
        for j in range(i, -1, -1):
            if sorting_list[j] > next_value:
                sorting_list[j+1] = sorting_list[j]
            else:
                break
        # here using the python for-else trick, since there is not j-- in for loop like in C language
        else:
            j = -1

        sorting_list[j+1] = next_value

# selection sort
# Ascending way
def selection_sort(sorting_list):
    length = len(sorting_list)
    for i in range(length):
        min_index = i
        for j in range(i+1, length):
            if sorting_list[j] < sorting_list[min_index]:
                min_index = j

        if min_index != i:
            # swap i-th element with min_index: j
            tmp = sorting_list[i]
            sorting_list[i] = sorting_list[min_index]
            sorting_list[min_index] = tmp



test_list = [6, 5, 4, 3, 2, 1]
bubble_sort(test_list)
print(test_list)

test_list = [2, 3, 1]
insertion_sort(test_list)
print(test_list)

test_list = [6, 5, 4, 3, 2, 1]
selection_sort(test_list)
print(test_list)
