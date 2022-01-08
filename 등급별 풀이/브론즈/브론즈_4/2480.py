arr = list(map(int, input().split()))
if arr[0] == arr[1] == arr[2]:
    print(10000 + arr[0]*1000)
elif arr[0] == arr[1]:
    print(1000 + arr[0]*100)
elif arr[1] == arr[2]:
    print(1000 + arr[1]*100)
elif arr[0] == arr[2]:
    print(1000 + arr[0]*100)
else:
    print(max(arr)*100)
    