# here value could be repeated in a list, no longer unique

# Firstly, find the first element which equals to value
def find_first_one(list_to_search, n, value):
    low = 0
    high = n - 1

    while low <= high:
        mid = low + ((high-low) >> 1)  # bitwise shift higher priority than plus(+)
        if list_to_search[mid] < value:
            low = mid +1
        elif list_to_search[mid] > value:
            high = mid -1
        else:
            if mid == 0 or list_to_search[mid-1] != value:
                return mid
            else:
                high = mid -1

    return None

# Secondly, find the last element which equals to value
def find_last_one(list_to_search, n, value):
    low = 0
    high = n - 1

    while low <= high:
        mid = low + ((high-low) >> 1)  # bitwise shift higher priority than plus(+)
        if list_to_search[mid] < value:
            low = mid + 1
        elif list_to_search[mid] > value:
            high = mid - 1
        else:
            if mid == n - 1 or list_to_search[mid+1] != value:
                return mid
            else:
                low = mid + 1

    return None

# Thirdly, find the first element which equals to or larger than value
def find_first_equal_and_larger_one(list_to_search, n, value):
    low = 0
    high = n - 1

    while low <= high:
        mid = low + ((high-low) >> 1)  # bitwise shift higher priority than plus(+)
        if list_to_search[mid] < value:
            low = mid + 1
        else:
            if mid == 0 or list_to_search[mid-1] < value:
                return mid
            else:
                high = mid - 1

    return None

# At last, find the last element which equals to or less than value
def find_last_equal_and_less_one(list_to_search, n, value):
    low = 0
    high = n - 1

    while low <= high:
        mid = low + ((high-low) >> 1)  # bitwise shift higher priority than plus(+)
        if list_to_search[mid] > value:
            high = mid-1
        else:
            if mid == n-1 or list_to_search[mid+1] > value:
                return mid
            else:
                low = mid + 1

    return None

my_list = [1,3,4,5,6,8,8,8,11,18]
my_set = set()
for value in my_list:
    if value not in my_set:
        my_set.add(value)
        print("{}: {}".format(value, find_first_one(my_list, len(my_list), value)))

print(find_last_one(my_list, len(my_list), 8))
print(find_first_equal_and_larger_one(my_list, len(my_list), 8))
print(find_last_equal_and_less_one(my_list, len(my_list), 8))