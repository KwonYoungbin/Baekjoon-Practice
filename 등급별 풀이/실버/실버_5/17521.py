day, money = map(int, input().split())
prices = [int(input()) for _ in range(day)]
coin = 0

for i in range(day-1):
    if coin == 0 and prices[i] < prices[i+1]:
        coin = money//prices[i]
        money %= prices[i]
    elif coin != 0 and prices[i] < prices[i+1]:
        continue
    elif coin != 0 and prices[i] > prices[i+1]:
        money += (coin*prices[i])
        coin = 0
        
print(money + coin*prices[-1])