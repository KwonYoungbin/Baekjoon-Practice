w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

x_move = (p+t) // w
y_move = (q+t) // h

result_x = (p+t) % w if x_move % 2 == 0 else w - (p+t) % w
result_y = (q+t) % h if y_move % 2 == 0 else h - (q+t) % h

print(result_x, result_y)