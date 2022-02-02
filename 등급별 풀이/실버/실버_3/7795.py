import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, M = map(int, input().rstrip().split())
    A = list(map(int, input().rstrip().split()))
    B = list(map(int, input().rstrip().split()))
    A.sort()
    B.sort()
    result = 0
    
    left = 0
    right = 0
    while left < N:
        if A[left] <= B[right]:
            left += 1
            result += right
        else:
            right += 1
            if right == M:
                result += (N - left) * right
                break
    print(result)