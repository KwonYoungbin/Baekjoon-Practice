import sys
input = sys.stdin.readline

M = int(input())
S = set()

for _ in range(M):
    command = input().split()
    if len(command) == 1:
        if command[0] == 'all':
            S = set([i for i in range(1, 21)])
        elif command[0] == 'empty':
            S = set()
            
    else:
        com, val = command
        val = int(val)
        
        if com == 'add':
            S.add(val)
        elif com == 'remove':
            S.discard(val)
        elif com == 'check':
            print(1 if val in S else 0) 
        elif com == 'toggle':
            if val in S:
                S.discard(val)
            else:
                S.add(val)