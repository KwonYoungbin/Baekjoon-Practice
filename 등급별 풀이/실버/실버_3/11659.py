import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
sum_list = [0]+[i for i in arr]

for i in range(2, N+1):
    sum_list[i] += sum_list[i-1]

for _ in range(M):
    left, right = map(int, input().rstrip().split())
    print(sum_list[right] - sum_list[left-1])