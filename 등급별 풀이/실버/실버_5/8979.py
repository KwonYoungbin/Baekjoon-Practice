n, k = map(int, input().split())
arr = []

for _ in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)
    
arr.sort(key=lambda x:(x[1], x[2], x[3]), reverse=True)

rank = [1] * (n+1)
for i in range(1, n):
    if arr[i][1] == arr[i-1][1] and arr[i][2] == arr[i-1][2] and arr[i][3] == arr[i-1][3]:
        rank[arr[i][0]] = rank[arr[i-1][0]]
    else:
        rank[arr[i][0]] = i+1
print(rank[k])