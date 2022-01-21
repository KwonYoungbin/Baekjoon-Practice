n = int(input())
word = list(input())
word.sort()
length = len(word)
cnt = 0

for _ in range(n-1):
    cmp = input()
    
    if abs(len(cmp) - length) > 1:
        continue
    else:
        if length == len(cmp):
            miss = 0
            for w in word:
                if w in cmp:
                    cmp = cmp.replace(w, '', 1)
                else:
                    miss += 1
            if miss <= 1:
                cnt += 1
        else:
            miss = 0
            for w in word:
                if w in cmp:
                    cmp = cmp.replace(w, '', 1)
                else:
                    miss += 1
            if len(cmp) + miss <= 1:
                cnt += 1
print(cnt)