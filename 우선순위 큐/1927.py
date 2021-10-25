import heapq
import sys

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, num)
    else:
        print(heapq.heappop(heap)) if heap else print(0)
