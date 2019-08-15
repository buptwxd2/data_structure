def square_root(value):
    low = 0
    high = value
    mid = (low + high)/2

    count = 0
    while abs(mid ** 2 - value) > 0.000001:
        if mid ** 2 - value < 0:
            low = mid
        elif mid ** 2 - value > 0:
            high = mid
        else:
            return mid

        mid = (low+high)/2
        count +=1

    print("Count is {}".format(count))
    return mid

print(square_root(9))