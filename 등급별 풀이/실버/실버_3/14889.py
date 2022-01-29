def dfs(idx, team1):
    global result
    
    if idx == N//2:
        team2 = [i for i in range(N) if i not in team1]
        sum_team1, sum_team2 = 0, 0
        for i in range(0, idx-1):
            for j in range(i+1, idx):
                sum_team1 += graph[team1[i]][team1[j]] + graph[team1[j]][team1[i]]
                sum_team2 += graph[team2[i]][team2[j]] + graph[team2[j]][team2[i]]
        diff = abs(sum_team1-sum_team2)
        if result > diff:
            result = diff
        return
    
    for i in range(idx, N):
        if i in team1: continue
        if len(team1) > 0 and team1[len(team1)-1] > i : continue
        team1.append(i)
        dfs(idx+1, team1)
        team1.pop()
        
        
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
result = int(1e9)

dfs(0, [])
print(result)