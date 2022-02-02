from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    dic = defaultdict(int)
    while n > 1:
        for i in range(2, n+1):
            if n % i == 0:
                dic[i] += 1
                n //= i
                break
    dic = dic.items()
    
    for row in dic:
        print(*row)