# try backtracking first

my_list = [2, 9, 3, 6, 5, 1, 7]
max_len = 0
max_sub = []

def f(i, current_sub):
    total_len = len(my_list)
    global max_len
    global max_sub

    if i == total_len:
        if len(current_sub) > max_len:
            max_len = len(current_sub)
            max_sub = current_sub

        return

    # NOT add the i-th element
    f(i+1, current_sub)
    # Add the i-th element
    if not current_sub:
        f(i+1, current_sub=[my_list[i]])
    else:
        if my_list[i] <= current_sub[-1]:
            return
        else:
            new_list = current_sub.copy()
            new_list.append(my_list[i])
            f(i+1, current_sub=new_list)

f(0, [])
print(max_len)
print(max_sub)