import heapq
import sys

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    num = int(sys.stdin.readline())
    if num != 0:
        # 튜플을 이용하여 정렬 가능 / 이때, 첫번째 요소를 기준으로 정렬됨
        heapq.heappush(heap, (abs(num), num))
    else:
        print(heapq.heappop(heap)[1]) if heap else print(0)
