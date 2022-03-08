from collections import deque

N, M = map(int, input().split())
train = [deque([0]*20) for _ in range(N)]

for _ in range(M):
    command = list(map(int, input().split()))
    if command[0] == 1:
        if train[command[1]-1][command[2]-1] == 0:
            train[command[1]-1][command[2]-1] = 1
    elif command[0] == 2:
        if train[command[1]-1][command[2]-1] == 1:
            train[command[1]-1][command[2]-1] = 0
    elif command[0] == 3:
        train[command[1]-1].pop()
        train[command[1]-1].appendleft(0)
    else:
        train[command[1]-1].popleft()
        train[command[1]-1].append(0)

result = []
for row in train:
    if row not in result:
        result.append(row)

print(len(result))