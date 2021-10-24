n = int(input())
scores = list(map(int,input().split()))
m = max(scores)

for i in range(n):
    scores[i] = (scores[i]/m)*100
    
print(sum(scores)/n)