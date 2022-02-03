import heapq

N, M = map(int, input().split())
needs = []
result = 0
for _ in range(N):
    p, l = map(int, input().split())
    miles = list(map(int, input().split()))
    if p < l:
        needs.append(1)
    else:
        miles.sort(reverse=True)
        needs.append(miles[l-1])

heapq.heapify(needs)
while needs:
    now = heapq.heappop(needs)
    if M - now < 0:
        break
    M -= now
    result += 1
print(result)