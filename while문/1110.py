num = int(input())
now = num
count = 0
while True:
    if now//10 == 0:
        now = now*10 + now
    else:
        new_val = ((now//10) + (now%10)) % 10
        now = ((now%10)*10) + new_val
    count += 1
    
    if num == now:
        print(count)
        break