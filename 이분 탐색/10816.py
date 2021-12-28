from collections import Counter

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
m_list = map(int, input().split())

counter = Counter(arr)
for val in m_list:
    print(counter[val], end=' ')