from collections import deque

number = int(input())

for _ in range(number):
    count = 0
    n, pos = map(int, input().split())
    priority = deque([[x,y] for x,y in enumerate(list(map(int, input().split())))])

    while True:
        cursor = priority.popleft()
        if any(cursor[1] < compare[1] for compare in priority):
            priority.append(cursor)
        else:
            count += 1
            if cursor[0] == pos:
                print(count)
                break