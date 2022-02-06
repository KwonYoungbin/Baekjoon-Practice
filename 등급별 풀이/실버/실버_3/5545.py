N = int(input())
A, B = map(int, input().split())
C = int(input())
topping = [int(input()) for _ in range(N)]
topping.sort(reverse=True)

max_cal = C // A

topping_cnt = 0
for t in topping:
    if (C + t) // (A + B*(topping_cnt+1)) >= max_cal:
        max_cal = (C + t) // (A + B*(topping_cnt+1))
        C += t
        topping_cnt += 1
    else:
        break
print(max_cal)