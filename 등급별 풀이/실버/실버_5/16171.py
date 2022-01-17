number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

S = input()
K = input()

for num in number:
    S = S.replace(num, '')

print(1 if K in S else 0)