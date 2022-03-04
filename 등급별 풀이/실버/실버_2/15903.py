import heapq

n, m = map(int, input().split())
arr = list(map(int, input().split()))
heapq.heapify(arr)

for _ in range(m):
    first = heapq.heappop(arr)
    second = heapq.heappop(arr)
    heapq.heappush(arr, first+second)
    heapq.heappush(arr, first+second)
    
print(sum(arr))