n, m = map(int, input().split())
prices = [int(input()) for _ in range(m)]
prices.sort(reverse=True)

result = 0
max_price = 0

for i in range(min(n, m)):
    if prices[i]*(i+1) > result:
        max_price = prices[i]
        result = prices[i]*(i+1)
print(max_price, result)