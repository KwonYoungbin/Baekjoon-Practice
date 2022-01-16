n = int(input())
start, end = 0, 1
total = 1
cnt = 1

while start <= n//2:
    if total < n:
        end += 1
        total += end
    elif total == n:
        cnt += 1
        end += 1
        total = total - start + end
        start += 1
    else:
        total -= start
        start += 1
print(cnt)