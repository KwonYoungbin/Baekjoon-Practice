import sys

n = int(sys.stdin.readline())
dist = list(map(int, sys.stdin.readline().split()))+[0]
prices = list(map(int, sys.stdin.readline().split()))
result = 0

minIdx = 0
km = dist[0]
for i in range(1,n):
    if prices[i] < prices[minIdx] or i == n-1:
        result += (prices[minIdx] * km)
        minIdx = i
        km = dist[i]
    else:
        km += dist[i]
print(result)