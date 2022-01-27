alphabet = 'abcdefghijklmnopqrstuvwxyz'
n = int(input())
arr = []

for _ in range(n):
    line = input()
    for w in alphabet:
        line = line.replace(w, ' ').replace('  ', ' ')
    arr += list(map(int, line.split()))
    
arr.sort()
print(*arr, sep='\n')