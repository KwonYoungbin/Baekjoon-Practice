n = int(input())
dp = 5
adder = 7

for _ in range(2, n+1):
    dp += adder
    adder += 3
print(dp % 45678)