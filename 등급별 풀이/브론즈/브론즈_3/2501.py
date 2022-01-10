n, k = map(int, input().split())
arr = []

for i in range(1, int(n**(1/2))+1):
    if n % i == 0:
        arr.append(i)
        if n//i not in arr:
            arr.append(n//i)
arr.sort()

if k > len(arr):
    print(0)
else:
    print(arr[k-1])