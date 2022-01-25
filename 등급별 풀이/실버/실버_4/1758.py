import sys
input = sys.stdin.readline

n = int(input())
tips = [int(input()) for _ in range(n)]
tips.sort(reverse=True)

result = 0
for i in range(n):
    tip = tips[i] - i
    result += tip if tip > 0 else 0
print(result)