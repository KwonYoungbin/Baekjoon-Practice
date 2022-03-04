moves = [(1,0), (0,1), (-1,0), (0,-1)]

def dfs(x, y, string, length):
    global result
    if length == 6:
        result.add(string)
        return
    
    for move in moves:
        nx = x + move[0]
        ny = y + move[1]
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, string+graph[nx][ny], length+1)
    

graph = [list(input().split()) for _ in range(5)]
result = set()

for x in range(5):
    for y in range(5):
        dfs(x, y, '', 0)
        
print(len(result))