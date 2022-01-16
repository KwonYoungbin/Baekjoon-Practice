vowel = ['a','e','i','o','u']

while True:
    string = input()
    if string == 'end':
        break
    
    chk = []
    acceptable = True
    
    for i in range(1, len(string)):
        if string[i] == string[i-1] and string[i] != 'e' and string[i] != 'o':
            acceptable = False
            break
    
    for s in string:
        if s in vowel:
            chk.append(-1)
        else:
            chk.append(1)
    
    if -1 not in chk:
        acceptable = False
    elif len(string) > 2:
        for i in range(3, len(string)+1):
            if sum(chk[i-3:i]) == 3 or sum(chk[i-3:i]) == -3:
                acceptable = False
                break
    
    if acceptable:        
        print("<%s> is acceptable." %(string))
    else:
        print("<%s> is not acceptable." %(string))