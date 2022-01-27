for _ in range(int(input())):
    sounds = input().split()
    while True:
        now = input()
        if now == 'what does the fox say?':
            print(' '.join(sounds))
            break
        
        now = now.split()[-1]
        while now in sounds:
            sounds.remove(now)    