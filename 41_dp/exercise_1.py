# try backtracking first
import math
total = 100
min_num = math.inf

mem = [[False] * (total+5) for _ in range(total+5)]        # row: total+1; column: total+1

def f(i, current_m):        # i是已投硬币的个数（第i次投币）， current_m是在投第i没硬币的时候已凑成的钱
    if mem[i][current_m] != 0:
        return

    global min_num
    if current_m >= total:
        if current_m == total:
            if i < min_num:
                min_num = i
        return

    mem[i][current_m] = True  # calcualted
    # 1 块
    f(i+1, current_m+1)
    # 3 块
    f(i+1, current_m+3)
    # 5 块
    f(i+1, current_m+5)

f(0, 0)
print(min_num)