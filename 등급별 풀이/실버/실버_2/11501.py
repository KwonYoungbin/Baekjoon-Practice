for _ in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    
    result = 0
    now_max = 0
    for i in range(N-1, -1, -1):
        if arr[i] > now_max:
            now_max = arr[i]
        else:
            result += (now_max-arr[i])
    print(result)