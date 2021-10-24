import sys

def get_gcd(a, b):
    x, y = b, a
    while y:
        x, y = y, x%y
    return x

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    arr.append(int(sys.stdin.readline()))
arr.sort()

#계산식에 따르면 정렬된 리스트의 연속된 두 값의 차이들의 최대공약수를 찾아야 함.
#모든 차의 최대공약수를 구한 이후, 최대공약수의 약수를 계산
gcd = arr[1] - arr[0]
for i in range(2, n):
    gcd = get_gcd(gcd, arr[i]-arr[i-1])

result = [gcd]
for num in range(2, int(gcd**(1/2))+1):
    if gcd % num == 0:
        result.append(num)
        if gcd // num != num:
            result.append(gcd // num)
result.sort()
print(*result, sep=' ')