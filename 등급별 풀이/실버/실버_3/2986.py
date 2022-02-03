n = int(input())
result = 0
divides = []

for i in range(1, int(n**(0.5))+1):
    if n % i == 0:
        divides.append(i)
        divides.append(n//i)
divides.sort()
print(divides[-1]-divides[-2])