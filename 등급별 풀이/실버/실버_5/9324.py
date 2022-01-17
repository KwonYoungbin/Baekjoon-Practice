t = int(input())

for _ in range(t):
    s = input()
    dic = {}
    idx = 0
    possible = True
    while idx < len(s):
        if s[idx] not in dic:
            dic[s[idx]] = 1
        else:
            dic[s[idx]] += 1
            
        if dic[s[idx]] % 3 == 0:
            if idx == len(s)-1 or s[idx] != s[idx+1]:
                possible = False
                break
            else:
                dic[s[idx]] = 0
                idx += 1
        idx += 1
    
    print('OK' if possible else 'FAKE')