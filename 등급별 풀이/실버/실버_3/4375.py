while True:
    try:
        n = int(input())
        now = '1'
        while True:
            if int(now)%n == 0:
                print(len(now))
                break
            else:
                now += '1'
    except EOFError:
        break