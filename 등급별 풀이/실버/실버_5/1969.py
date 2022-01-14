n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
result = ''
dist = 0

for i in range(m):
    dic = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for j in range(n):
        dic[arr[j][i]] += 1
    dic = sorted(dic.items(), key=lambda x:(-x[1], x[0]))
    result += dic[0][0]
    dist += (n - dic[0][1])
    
print(result, dist, sep='\n')