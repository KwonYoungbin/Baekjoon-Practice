import sys
input = sys.stdin.readline

n, m = map(int, input().split())
imp = [[True]*n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    imp[a-1][b-1] = False
    imp[b-1][a-1] = False

result = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if imp[i][j] and imp[i][k] and imp[j][k]:
                result += 1
print(result)