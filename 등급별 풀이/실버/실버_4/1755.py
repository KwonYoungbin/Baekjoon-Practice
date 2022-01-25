from collections import defaultdict

M, N = map(int, input().split())
words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
dic = defaultdict()

for i in range(M, N+1):
    w = str(i)
    temp = ''
    for val in w:
        temp += words[int(val)] + ' '
    dic[i] = temp
dic = sorted(dic.items(), key=lambda x:x[1])

for i in range(1, len(dic)+1):
    print(dic[i-1][0], end=' ')
    if i%10 == 0:
        print()