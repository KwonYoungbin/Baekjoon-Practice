M = int(input())
count = list(map(int, input().split()))
K = int(input())

if M == 1 or K == 1:
    print(1.0)
else:
    result = 0
    total = sum(count)
    for c in count:
        if c >= K:
            temp = 1
            for i in range(K):
                temp *= ((c-i)/(total-i))
            result += temp
    print(result)