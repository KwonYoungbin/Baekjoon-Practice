N, K = map(int, input().split())
S = list(input())
result = 0

for i in range(N):
    if S[i] == 'P':
        for j in range(-K, K+1):
            nx = i + j
            if 0 <= nx < N:
                if S[nx] == 'H':
                    result += 1
                    S[nx] = 'X'
                    break
print(result)