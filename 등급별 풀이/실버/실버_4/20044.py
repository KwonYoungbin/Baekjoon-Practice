n = int(input())
arr = list(map(int, input().split()))
arr.sort()

team_level = []

for i in range(n):
    team_level.append(arr[i]+arr[2*n-1-i])
print(min(team_level))