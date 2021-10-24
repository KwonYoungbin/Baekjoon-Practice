n = input()
arr = []

for i in n:
    if i >= 'A' and i <= 'C':
        arr.append(2)
    elif i >= 'D' and i <= 'F':
        arr.append(3)
    elif i >= 'G' and i <= 'I':
        arr.append(4)
    elif i >= 'J' and i <= 'L':
        arr.append(5)
    elif i >= 'M' and i <= 'O':
        arr.append(6)
    elif i >= 'P' and i <= 'S':
        arr.append(7)
    elif i >= 'T' and i <= 'V':
        arr.append(8)
    elif i >= 'W' and i <= 'Z':
        arr.append(9)
print(sum(arr)+len(n))