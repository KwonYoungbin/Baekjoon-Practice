N, K = map(int, input().split())
pattern = [input().split() for _ in range(K)]
pattern.reverse()
arr = ['?'] * N

now = 0
impossible = False
for num, al in pattern:
    if arr[now] == al:
        pass
    elif arr[now] == '?':
        if al in arr:
            impossible = True
            break
        arr[now] = al
    else:
        impossible = True
        break
    now += int(num)
    now %= N
    
print('!' if impossible else ''.join(arr))