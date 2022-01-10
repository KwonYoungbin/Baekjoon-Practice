n = int(input())

for i in range(1, n+1):
    arr = ['*'] * i
    print((' '*(n-i)) + ' '.join(arr))