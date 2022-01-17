while True:
    n = int(input())
    if n == 0:
        break
    
    words = [input() for _ in range(n)]
    words.sort(key=lambda x:x.lower())
    print(words[0])