x = list(map(int, input()))
cnt = 0

while len(x) > 1:
    x = list(map(int, str(sum(x))))
    cnt += 1
    
if x[0] % 3 == 0:
    print(cnt, 'YES', sep='\n')
else:
    print(cnt, 'NO', sep='\n')