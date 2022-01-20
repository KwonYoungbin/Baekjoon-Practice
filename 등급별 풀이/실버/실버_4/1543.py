doc = input()
word = input()

idx = 0
l = len(word)
cnt = 0
while idx <= len(doc)-l:
    if doc[idx:idx+l] == word:
        cnt += 1
        idx += l
    else:
        idx += 1
print(cnt)