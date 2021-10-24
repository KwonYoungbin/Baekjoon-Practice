n = int(input())

for i in range(n):
    data = list(map(int,input().split()))
    avg = sum(data[1:]) / data[0]
    count = 0
    for j in data[1:]:
        if j > avg:
            count += 1
    print("%.3f%%"%round((count/data[0])*100, 3))