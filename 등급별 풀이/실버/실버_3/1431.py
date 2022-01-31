N = int(input())
dic = {}

for _ in range(N):
    S = input()
    cnt = 0
    for s in S:
        if s.isdigit():
            cnt += int(s)
    dic[S] = cnt

dic = sorted(dic.items(), key=lambda x:(len(x[0]), x[1], x[0]))

for i in range(N):
    print(dic[i][0])