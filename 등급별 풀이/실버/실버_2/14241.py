N = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
result = 0

while len(arr) > 1:
    left = arr.pop()
    right = arr.pop()
    result += (left*right)
    arr.append(left+right)
print(result)