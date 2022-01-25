n = int(input())
arr = [1]

for i in range(1, n+1):
    now = 0
    for j in range(i):
        now += arr[j]*arr[i-j-1]
    arr.append(now)
print(arr[n])