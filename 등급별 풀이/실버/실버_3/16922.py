N = int(input())
roma = [1, 5, 10, 50]
result = [set() for _ in range(N+1)]
result[1] = set(roma)

for i in range(2, N+1):
    temp = result[i-1]
    r = set()
    for t in temp:
        for k in roma:
            r.add(t+k)
    result[i] = r
print(len(result[N]))