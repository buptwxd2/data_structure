# 顺序存储线性表 using python array/list
from array import *

def my_insert(arr, i, value):
    original_length = len(arr)

    if i > len(arr):
        print("")
        return None

    # add a new element size first
    arr.append(None)
    idx = original_length - 1
    while idx >= i:
        arr[idx+1] = arr[idx]
        idx = idx - 1

    arr[i] = value

    return arr

def my_delete(arr, value):
    # remove the first item equals with value
    if not arr:
        print("Empty list.")
        return None

    original_length = len(arr)
    idx = 0
    while idx < original_length:
        if arr[idx] == value:
            start_to_copy = idx
            while start_to_copy < original_length -1:
                arr[start_to_copy] = arr[start_to_copy+1]
                start_to_copy = start_to_copy + 1

            del arr[-1]
            break

        idx = idx + 1

    return arr

def my_search(arr, value):
    original_length = len(arr)
    if original_length == 0:
        return None

    idx = 0
    while idx < original_length:
        if arr[idx] == value:
            return idx

        idx = idx + 1

    return None

def my_update(arr, i, new_value):
    original_length = len(arr)

    if i < 0 or i >= original_length:
        return None

    arr[i] = new_value

    return arr

array1 = [0, 1, 2, 3, 4]
print (array1)
my_insert(array1, 5, 100)
print (array1)
my_delete(array1, 40)
print (array1)
print ("Index of value {} is {}".format(4, my_search(array1, 100)))

my_update(array1, 6, 200)
print (array1)