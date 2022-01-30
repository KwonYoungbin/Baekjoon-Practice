N = int(input())
S = input()
dic = {}

for i in range(ord('A'), ord('A')+N):
    dic[chr(i)] = int(input())

operand = []
for s in S:
    if s.isalpha():
        operand.append(dic[s])
    else:
        right = operand.pop()
        left = operand.pop()
        if s == '+':
            operand.append(left+right)
        elif s == '-':
            operand.append(left-right)
        elif s == '*':
            operand.append(left*right)
        elif s == '/':
            operand.append(left/right)
print("{:.2f}".format(operand[0]))