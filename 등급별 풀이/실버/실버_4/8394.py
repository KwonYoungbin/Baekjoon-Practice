n = int(input())
arr = [0,0,2,3]
for i in range(4, n+1):
    arr.append((arr[-2] + arr[-1])%10)
print(arr[n])