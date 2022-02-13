N = int(input())
arr = list(map(int, input().split()))
total_arr = [i for i in arr]

for i in range(1, N):
    for j in range(i-1, -1, -1):
        if arr[j] < arr[i]:
            total_arr[i] = max(total_arr[i], arr[i]+total_arr[j])

print(max(total_arr))