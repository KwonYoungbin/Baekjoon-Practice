n, k = map(int, input().split())
tempo = list(map(int, input().split()))
sum_temp = []
for i in range(k, n+1):
    sum_temp.append(sum(tempo[i-k:i]))
print(max(sum_temp))