T = int(input())
if T%10 != 0:
    print(-1)
else:
    print(T//300, end=' ')
    T %= 300
    print(T//60, end=' ')
    T %= 60
    print(T//10, end=' ')