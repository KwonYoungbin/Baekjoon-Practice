n = int(input())
m = int(input())
material = list(map(int, input().split()))
material.sort()

cnt = 0
left = 0
right = n-1

while left < right:
    cal = material[left] + material[right]
    if cal == m:
        cnt += 1
        left += 1
        right -= 1
    elif cal > m:
        right -= 1
    elif cal < m:
        left += 1
print(cnt)