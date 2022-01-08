prices = [int(input()) for _ in range(5)]
print(min(prices[:3]) + min(prices[3:]) - 50)