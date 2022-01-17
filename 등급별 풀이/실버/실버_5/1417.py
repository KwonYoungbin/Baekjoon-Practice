n = int(input())
arr = [int(input()) for _ in range(n)]

if len(arr) == 1:
    print(0)
else:
    temp = sorted(arr[1:])
    cnt = 0

    while arr[0] <= temp[-1]:
        arr[0] += 1
        temp[-1] -= 1
        temp.sort()
        cnt+=1
    print(cnt)