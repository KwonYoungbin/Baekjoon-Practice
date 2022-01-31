N, L = map(int, input().split())
pos = list(map(int, input().split()))
pos.sort()

result = 0
left = 0
right = 0
while left < N:
    if right >= N:
        result += 1
        break
    
    if pos[right] - pos[left] <= L-1:
        right += 1
    else:
        result += 1
        left = right
print(result)