string = input().upper()
list_set = list(set(string))
cnt = []

for i in list_set:
    cnt.append(string.count(i))
    
if cnt.count(max(cnt)) > 1:
    print('?')
else:
    print(list_set[cnt.index(max(cnt))])