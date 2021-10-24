import sys

def factorial(num):
    result = 1
    for i in range(1,num+1):
        result *= i
    return result

n = int(sys.stdin.readline())
arr = list(map(int, str(factorial(n))))
arr.reverse()

for i in range(len(arr)):
    if arr[i] != 0:
        print(i)
        break