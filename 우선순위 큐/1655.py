import heapq
import sys

n = int(sys.stdin.readline())
left = []
right = []

# 이해 X / 다시 한번 학습해야 함.
for _ in range(n):
    num = int(sys.stdin.readline())
    if len(left) == len(right):
        heapq.heappush(left, (-num, num))
    else:
        heapq.heappush(right, (num, num))

    if right and left[0][1] > right[0][1]:
        l_v = heapq.heappop(left)[1]
        r_v = heapq.heappop(right)[1]
        heapq.heappush(right, (l_v, l_v))
        heapq.heappush(left, (-r_v, r_v))
    
    print(left[0][1])