from collections import deque
from itertools import permutations

n = int(input())
nPr = deque(list(permutations([1,2,3,4,5,6,7,8,9], 3)))

for _ in range(n):
    val, strike, ball = map(int, input().split())
    val = list(map(int, str(val)))
    
    for i in range(len(nPr)):
        s_cnt, b_cnt = 0, 0
        now = nPr.popleft()
        
        for j in range(3):
            if val[j] in now and val[j] == now[j]:
                s_cnt += 1
            elif val[j] in now and val[j] != now[j]:
                b_cnt += 1
                
        if s_cnt == strike and b_cnt == ball:
            nPr.append(now)
print(len(nPr))