n = list(input())

if sum(int(i) for i in n) % 3 != 0 or '0' not in n:
    print(-1)
else:
    n.sort(reverse=True)
    print(''.join(n))