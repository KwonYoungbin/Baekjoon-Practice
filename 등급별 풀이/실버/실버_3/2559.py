N, K = map(int, input().split())
tempo = list(map(int, input().split()))

left = 0
right = K
total = [sum(tempo[:K])]
while right < N:
    total.append(total[-1] - tempo[left] + tempo[right])
    left += 1
    right += 1
print(max(total))