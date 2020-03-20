# then try dp 状态转移方程

a = 'abcabc'
b = 'a'
import  math
min_distance = math.inf


def min_dist(a, b):
    if not a or not b:
        return len(a) or len(b)

    if a[-1] == b[-1]:
        return min(min_dist(a[:-1], b[:-1]), min_dist(a[:-1], b)+1, min_dist(a, b[:-1])+1)
    else:
        return min(min_dist(a[:-1], b[:-1]), min_dist(a[:-1], b), min_dist(a, b[:-1])) + 1

print(min_dist(a, b))
