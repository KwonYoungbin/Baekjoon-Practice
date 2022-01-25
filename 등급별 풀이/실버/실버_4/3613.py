def ctoj(s):
    if s[0] == '_' or s[-1] == '_' or '__' in s:
        return 'Error!'
    
    result = ''
    next_upper = False
    for val in s:
        if val.isupper():
            return 'Error!'
        
        if next_upper:
            result += val.upper()
            next_upper = False
        elif val == '_':
            next_upper = True
        else:
            result += val
    return result
            
def jtoc(s):
    if s[0].isupper():
        return 'Error!'

    result = ''
    for val in s:
        if val.isupper():
            result += '_'+val.lower()
        else:
            result += val
    return result

                
s = input()
if '_' in s:
    print(ctoj(s))
else:
    print(jtoc(s))