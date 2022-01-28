A = int(input())
X = int(input())
result = 1

arr = [A]
for i in range(64):
    arr.append(arr[-1]**2 % 1000000007)

X = bin(X)[2:][::-1]
for i in range(len(X)):
    if X[i] == '1':
        result *= arr[i]
print(result%1000000007)