def permutation(n):
    if n == 1:
        return [[1]]

    else:
        return [sub_list + [i+1] for i in range(n) for sub_list in permutation(n-1)]

print(permutation(2))
