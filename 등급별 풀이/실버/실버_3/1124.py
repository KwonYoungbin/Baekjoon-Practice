A, B = map(int, input().split())
prime_chk = [True] * 100001
prime_chk[0] = prime_chk[1] = False
for i in range(2, 50001):
    if prime_chk[i]:
        for j in range(2, 50001):
            if i*j > 100000:
                break
            prime_chk[i*j] = False

arr = [0]*100001
for i in range(1, B+1):
    if prime_chk[i]:
        arr[i] = 1
        
for i in range(2, B+1):
    for j in range(2, B+1):
        if i*j > B:
            break
        arr[i*j] = arr[i] + 1

result = 0
for i in range(A, B+1):
    if prime_chk[arr[i]]:
        result += 1
print(result)