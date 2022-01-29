S = input().replace('()', '-')

now = 0
result = 0

for s in S:
    if s == '-':
        result += now
    elif s == '(':
        now += 1
    elif s == ')':
        result += 1
        now -= 1
print(result)