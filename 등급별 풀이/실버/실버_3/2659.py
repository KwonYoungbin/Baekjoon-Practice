def cal_min(val):
    num_list = []
    for _ in range(4):
        num_list.append(val)
        val = (val%1000)*10 + val//1000
    return min(num_list)

N = cal_min(int(''.join(input().split())))

cnt = 0
for i in range(1111, N+1):
    if '0' not in str(i):
        if cal_min(i) == i:
            cnt += 1
print(cnt)