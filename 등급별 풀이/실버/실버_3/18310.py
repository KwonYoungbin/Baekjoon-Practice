N = int(input())
home = list(map(int, input().split()))
home.sort()
mid = home[(N-1)//2]
result = 0
print(mid)