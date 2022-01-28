N, K = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(N)]
ice.sort(key=lambda x:x[1])

total = 0
left, right = 0, 1
temp = ice[left][0]
while left < N and right < N:
    if ice[right][1] - ice[left][1] <= 2*K:
        temp += ice[right][0]
        if temp > total:
            total = temp
        right += 1
    else:
        temp -= ice[left][0]
        left += 1
print(total)