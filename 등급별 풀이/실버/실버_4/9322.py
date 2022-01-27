for _ in range(int(input())):
    n = int(input())
    PSA1 = input().split()
    PSA2 = input().split()
    security = input().split()
    pattern = []
    for word in PSA1:
        pattern.append(PSA2.index(word))
    
    result = [security[i] for i in pattern]
    print(*result)