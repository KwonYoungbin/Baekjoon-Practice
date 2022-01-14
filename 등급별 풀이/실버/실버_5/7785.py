import sys
input = sys.stdin.readline

n = int(input())
arr = set()

for _ in range(n):
    name, com = input().split()
    if name in arr:
        arr.discard(name)
    else:
        arr.add(name)

print(*sorted(arr, reverse=True), sep='\n')