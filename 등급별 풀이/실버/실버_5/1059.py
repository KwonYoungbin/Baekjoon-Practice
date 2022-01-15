L = int(input())
arr = [0] + list(map(int, input().split()))
n = int(input())

start, end = 0, 0
arr.sort()

if n in arr:
    print(0)
else:
    for i in range(L):
        if arr[i] < n < arr[i+1]:
            start = arr[i]+1
            end = arr[i+1]-1
            break
        
    print((end-start) + ((n-start) * (end-n)))