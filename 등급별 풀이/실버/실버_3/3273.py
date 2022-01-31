n = int(input())
arr = sorted(list(map(int, input().split())))
X = int(input())

result = 0
left = 0
right = n-1
while left < right:
    cal = arr[left] + arr[right]
    if cal == X:
        result += 1
        left += 1
    elif cal > X:
        right -= 1
    else:
        left += 1
print(result)