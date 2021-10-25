import heapq
import sys

n = int(sys.stdin.readline())
heap = []

# heapq 모듈은 최소힙만 제공하므로 -1을 곱하여 최대값 구하기 가능
for _ in range(n):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, -1*num)
    else:
        print(-1*heapq.heappop(heap)) if heap else print(0)
