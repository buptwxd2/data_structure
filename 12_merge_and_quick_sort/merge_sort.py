# mainly includes merge sort


# merge two sorted list
def merge(list_1, list_2):
    if not list_1:
        return list_2

    if not list_2:
        return list_1

    merged_list = []
    i = 0
    j = 0
    while i < len(list_1) and j < len(list_2):
        if list_1[i] <= list_2[j]:
            merged_list.append(list_1[i])
            i += 1
        else:
            merged_list.append(list_2[j])
            j += 1

    if i == len(list_1):
        merged_list += list_2[j:]
        return merged_list

    if j == len(list_2):
        merged_list += list_1[i:]
        return merged_list


def merge_sort(list_to_sort):
    if len(list_to_sort) == 0 or len(list_to_sort) == 1:
        return list_to_sort

    middle = len(list_to_sort) // 2

    return merge(merge_sort(list_to_sort[:middle]), merge_sort(list_to_sort[middle:]))

print(merge([1, 3, 5], [2, 4, 6]))
print(merge([5], [7]))

print(merge_sort([6, 4, 5, 7, 3, 2, 10, 1]))