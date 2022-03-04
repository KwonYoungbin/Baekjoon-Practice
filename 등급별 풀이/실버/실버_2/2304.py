from collections import deque

N = int(input())
pillar = deque(sorted([list(map(int, input().split())) for _ in range(N)]))
result = []
prev_pos, prev_h = 0, 0

while pillar:
    pos, h = pillar.popleft()

    if h < prev_h:
        continue

    prev_pos, prev_h = pos, h
    flag = False
    for nxt_pos, nxt_h in pillar:
        if nxt_h > h:
            result.append((nxt_pos-pos)*h)
            flag = True
            break
    
    if not flag:
        result.append(h)
        prev_pos += 1
        break

while pillar:
    pos, h = pillar.popleft()
    is_max = True
    
    for nxt_pos, nxt_h in pillar:
        if nxt_h > h:
            is_max = False
            break
        
    if is_max:
        result.append((pos-prev_pos+1)*h)
        prev_pos = pos+1
        
print(sum(result))