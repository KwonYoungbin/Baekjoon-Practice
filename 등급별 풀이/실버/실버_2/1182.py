def back(idx, total):
    global result
    if idx >= N:
        return
    
    total += numbers[idx]
    
    if total == S:
        result += 1
        
    back(idx+1, total)
    back(idx+1, total-numbers[idx])
            

result = 0
N, S = map(int, input().split())
numbers = list(map(int, input().split()))
back(0, 0)
print(result)