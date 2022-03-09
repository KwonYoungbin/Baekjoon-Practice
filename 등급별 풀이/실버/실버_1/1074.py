def recur(n, row, col):
    global result
    if n == 1:
        temp = [[0, 1], [2, 3]]
        result += temp[row][col]
        return
        
    x_pos = row//(2**(n-1))
    y_pos = col//(2**(n-1))
    nxt_x_pos = row%(2**(n-1))
    nxt_y_pos = col%(2**(n-1))
    
    if x_pos == 0 and y_pos == 0:
        # Left_Up
        recur(n-1, nxt_x_pos, nxt_y_pos)
    elif x_pos == 0 and y_pos == 1:
        # Right_Up
        result += (4**(n-1))
        recur(n-1, nxt_x_pos, nxt_y_pos)
    elif x_pos == 1 and y_pos == 0:
        # Left_Down
        result += (4**(n-1)*2)
        recur(n-1, nxt_x_pos, nxt_y_pos)
    elif x_pos == 1 and y_pos == 1:
        # Right_Down
        result += (4**(n-1)*3)
        recur(n-1, nxt_x_pos, nxt_y_pos)
    

N, R, C = map(int, input().split())
result = 0
recur(N, R, C)
print(result)