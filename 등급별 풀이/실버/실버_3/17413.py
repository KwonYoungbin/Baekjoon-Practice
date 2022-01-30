S = input()
stack = []
able = False
temp = []
result = ''

for s in S:
    if s == '<':
        if temp:
            result += ''.join(temp[::-1])
            temp = []
        result += '<'
        able = True
    elif s == '>':
        result += '>'
        able = False
    else:
        if able:
            result += s
        else:
            if s != ' ':
                temp.append(s)
            else:
                result += ''.join(temp[::-1]) + ' '
                temp = []
if temp:
    result += ''.join(temp[::-1])
print(result)