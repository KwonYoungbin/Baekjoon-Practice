from collections import Counter
S = input()
counter = Counter(S)
l = len(S)

if l % 2 == 0:
    possible = True
    for key in counter.keys():
        if counter[key] % 2 != 0:
            possible = False
            break
        
    if not possible:
        print('I\'m Sorry Hansoo')
    else:
        counter = sorted(counter.items(), key=lambda x:x[0])
        result = ''
        for w, num in counter:
            result += w*(num//2)
        result += result[::-1]
        print(result)
else:
    odd = 0
    odd_alpha = ''
    for key in counter.keys():
        if counter[key] % 2 != 0:
            odd += 1
            odd_alpha = key
            
    if odd != 1:
        print('I\'m Sorry Hansoo')
    else:
        counter = sorted(counter.items(), key=lambda x:x[0])
        result = ''
        for w, num in counter:
            result += w*(num//2)
        result += odd_alpha + result[::-1]
        print(result)