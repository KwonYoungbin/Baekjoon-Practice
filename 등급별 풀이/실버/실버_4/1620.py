import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dictionary = {}

for i in range(1, n+1):
    name = input().strip()
    dictionary[name] = i
    dictionary[i] = name
    
for _ in range(m):
    val = input().strip()
    if val.isdigit():
        print(dictionary[int(val)])
    else:
        print(dictionary[val])