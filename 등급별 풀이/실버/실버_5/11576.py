A, B = map(int, input().split())
m = int(input())
arr = list(map(int, input().split()))[::-1]

dec = 0
for idx, val in enumerate(arr):
    dec += (A**idx)*val

converted = []
while dec > 0:
    converted.append(dec%B)
    dec //= B
print(*converted[::-1])