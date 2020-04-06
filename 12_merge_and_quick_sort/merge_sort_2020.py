# 以前的merge_sort并不是sort in place的
# 此处尝试改为sort in place的

def merge_sort(list_to_sort, low, high):
    if low >= high:
        # actually i didn't find a chance that low will be higher than high, only equal is possible
        # 当只剩下一个元素时，自然就是已经排好序的
        return

    mid = (low+high) // 2

    merge_sort(list_to_sort, low, mid)
    merge_sort(list_to_sort, mid+1, high)
    merge(list_to_sort, low, mid, high)

    print(list_to_sort)
    return list_to_sort


def merge(list_to_sort, low, mid, high):
    # here we could not merge in place
    # instead we create a new list and override the original list
    tmp = []

    i = low
    j = mid+1
    while i <= mid and j <= high:
        if list_to_sort[i] <= list_to_sort[j]:
            tmp.append(list_to_sort[i])
            i += 1
        else:
            tmp.append(list_to_sort[j])
            j += 1

    if i <= mid:
        tmp.extend(list_to_sort[i:mid+1])

    if j <= high:
        tmp.extend(list_to_sort[j:high+1])

    list_to_sort[low:high+1] = tmp

test_list = [5,4, 3]
merge_sort(test_list, 0, 2)
