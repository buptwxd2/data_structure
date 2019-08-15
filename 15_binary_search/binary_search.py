# binary search, time complexity: O(logn)

#non-recursive way
def binary_search(list_to_search, n, value):
    # n is the range to search inside the list
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2
        if list_to_search[mid] == value:
            return mid
        elif list_to_search[mid] > value:
            high = high - 1
        elif list_to_search[mid] < value:
            low = low + 1

    # Could not find the target, return None
    return None

def recur_binary_search(list_to_search, low, high, value):
    if low > high:
        return None

    mid = (low+high)//2
    if list_to_search[mid] == value:
        return mid
    elif list_to_search[mid] > value:
        return recur_binary_search(list_to_search, low, mid-1, value)
    elif list_to_search[mid] < value:
        return recur_binary_search(list_to_search, mid+1, high, value)



my_list = [1, 3, 4, 5, 7, 9, 10]

for value in my_list:
    print(binary_search(my_list, len(my_list), value))

for value in my_list:
    print(recur_binary_search(my_list, 0, len(my_list)-1, value))
