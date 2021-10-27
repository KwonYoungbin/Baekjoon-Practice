import sys

zero = [1,0,1]
one = [0,1,1]

def fibonacci(n):
    for i in range(len(zero), n+1):
        zero.append(zero[i-2]+zero[i-1])
        one.append(one[i-2]+one[i-1])
    print("%d %d" %(zero[n], one[n]))

n = int(sys.stdin.readline())

for _ in range(n):
    fibonacci(int(sys.stdin.readline()))