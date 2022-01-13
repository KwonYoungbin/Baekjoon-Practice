N, W, H = map(int, input().split())
max_length = (W**2 + H**2)**(0.5)

for _ in range(N):
    a = int(input())
    if a <= max_length:
        print('DA')
    else:
        print('NE')