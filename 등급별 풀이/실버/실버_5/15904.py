String = input()
chk = ['U', 'C', 'P', 'C']
idx = 0
for s in String:
    if s == chk[idx]:
        idx += 1
        
        if idx > 3:
            break
        
if idx > 3:
    print('I love UCPC')
else:
    print('I hate UCPC')