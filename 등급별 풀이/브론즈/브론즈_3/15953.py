t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    result = 0
    
    if a == 1:
        result += 5000000
    elif 2 <= a <= 3:
        result += 3000000
    elif 4 <= a <= 6:
        result += 2000000
    elif 7 <= a <= 10:
        result += 500000
    elif 11 <= a <= 15:
        result += 300000
    elif 16 <= a <= 21:
        result += 100000
        
    if b == 1:
        result += 5120000
    elif 2 <= b <= 3:
        result += 2560000
    elif 4 <= b <= 7:
        result += 1280000
    elif 8 <= b <= 15:
        result += 640000
    elif 16 <= b <= 31:
        result += 320000
    
    print(result)