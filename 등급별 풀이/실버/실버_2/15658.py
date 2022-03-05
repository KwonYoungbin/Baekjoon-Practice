def back(now, idx):
    global max_result, min_result
    
    if idx == N:
        max_result = max(max_result, now)
        min_result = min(min_result, now)
        return
    
    if oper[0] > 0:
        oper[0] -= 1
        back(now+arr[idx], idx+1)
        oper[0] += 1
    if oper[1] > 0:
        oper[1] -= 1
        back(now-arr[idx], idx+1)
        oper[1] += 1
    if oper[2] > 0:
        oper[2] -= 1
        back(now*arr[idx], idx+1)
        oper[2] += 1
    if oper[3] > 0:
        oper[3] -= 1
        back(int(now/arr[idx]), idx+1)
        oper[3] += 1

N = int(input())
arr = list(map(int, input().split()))
oper = list(map(int, input().split()))
max_result, min_result = -int(1e9), int(1e9)

back(arr[0], 1)
print(max_result)
print(min_result)