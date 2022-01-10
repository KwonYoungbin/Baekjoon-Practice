arr = [sum(list(map(int, input().split()))) for _ in range(5)]
print(arr.index(max(arr))+1, max(arr))