N = int(input())
arr = list(map(int, input().split()))
INC = [1]*N
DEC = [1]*N

for i in range(1, N):
    if arr[i] >= arr[i-1]:
        INC[i] += INC[i-1]
    
    if arr[i] <= arr[i-1]:
        DEC[i] += DEC[i-1]
print(max(max(INC), max(DEC)))