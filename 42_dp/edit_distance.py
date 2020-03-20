# first try backtracking

a = 'abc'
b = 'c'
import  math
min_distance = math.inf

def f(i, j, current_distance):  # i: index of a; j: index of b; current_distance
    global min_distance
    len_a, len_b = len(a), len(b)

    if i == len(a):
        distance = current_distance + len_b -j
        if distance < min_distance:
            min_distance = distance
        return

    if j == len(b):
        distance = current_distance + len_a -i
        if distance < min_distance:
            min_distance = distance
        return

    if a[i] == b[j]:
        f(i+1, j+1, current_distance)
    else:
        f(i+1, j+1, current_distance+1)     #将a[i]和b[j]替换成一样的字符
        f(i, j+1, current_distance+1)       #删除b[j]或者a[i]前添加一个字符
        f(i+1, j, current_distance+1)       #删除a[i]或者b[j]前添加一个字符

f(0, 0, 0)
print(min_distance)