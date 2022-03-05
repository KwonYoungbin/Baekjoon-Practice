from collections import defaultdict

N = int(input())
M = int(input())
arr = list(map(int, input().split()))
dic = defaultdict()

for i in range(M):
    if arr[i] in dic:
        dic[arr[i]][0] += 1
    else:
        if len(dic) >= N:
            temp_list = sorted(dic.items(), key=lambda x:(x[1][0], x[1][1]))
            del_key = temp_list[0][0]
            del(dic[del_key])
        dic[arr[i]] = [1, i]
        
print(*sorted(list(dic.keys())))