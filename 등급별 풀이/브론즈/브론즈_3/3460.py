t = int(input())

for _ in range(t):
    n = int(input())
    arr = bin(n)[2:][::-1]
    
    temp = []
    for idx in range(len(arr)):
        if arr[idx] == '1':
            temp.append(str(idx))
    print(' '.join(temp))