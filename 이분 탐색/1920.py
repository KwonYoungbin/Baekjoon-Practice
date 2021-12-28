n = int(input())
a_list = list(map(int, input().split()))
m = int(input())
m_list = map(int, input().split())

a_list.sort()

for val in m_list:
    flag = False
    left = 0
    right = len(a_list)-1
    
    while left <= right:
        mid = (left+right) // 2
        if a_list[mid] == val:
            flag = True
            break
        elif a_list[mid] > val:
            right = mid - 1
        elif a_list[mid] < val:
            left = mid + 1
    print(1) if flag else print(0)