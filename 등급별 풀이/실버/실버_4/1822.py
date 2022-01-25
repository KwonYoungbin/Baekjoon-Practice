# 차집합을 이용해 푸는 방법
nA, nB = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
result = list(A-B)

if not result:
    print(0)
else:
    result.sort()
    print(len(result))
    print(*result)
    
# 이분 탐색을 이용해 푸는 방법  
# from collections import defaultdict

# nA, nB = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# A.sort()
# B.sort()
# result = []

# for a in A:
#     left = 0
#     right = nB-1
#     find = False
#     while left <= right:
#         mid = (left + right) // 2
#         if B[mid] == a:
#             find = True
#             break
#         elif B[mid] > a:
#             right = mid - 1
#         else:
#             left = mid + 1
            
#     if not find:
#         result.append(a)
# if not result:
#     print(0)
# else:
#     print(len(result))
#     print(*result)