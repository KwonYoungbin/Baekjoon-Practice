import sys
input = sys.stdin.readline

N, K, B = map(int, input().strip().split())
arr = [0]*(N+1)

for _ in range(B):
    arr[int(input())] = 1

total = sum(arr[:K+1])
result = B
for i in range(2, N-K+2):
    total = total-arr[i-1]+arr[i-1+K]
    result = min(result, total)
print(result)