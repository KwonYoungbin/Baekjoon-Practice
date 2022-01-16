import heapq

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
heapq.heapify(arr)

now = 0
while arr:
    start, end = heapq.heappop(arr)
    if now < start:
        now = start + end
    else:
        now += end
print(now)