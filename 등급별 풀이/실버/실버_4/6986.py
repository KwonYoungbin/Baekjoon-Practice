n, k = map(int, input().split())
score = [float(input()) for _ in range(n)]
score.sort()

subscore = score[k:n-k]
total = sum(subscore)

print('{:.2f}'.format((total / (n-2*k))+ 0.00000001))
print('{:.2f}'.format(((total+(subscore[0]*k)+(subscore[-1]*k))/n + 0.00000001)))