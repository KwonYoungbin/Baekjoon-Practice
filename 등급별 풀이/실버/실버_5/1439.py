S = input()
while '11' in S or '00' in S:
    S = S.replace('11','1').replace('00','0')

if len(S) == 1:
    print(0)
else:
    print(min(S.count('0'), S.count('1')))