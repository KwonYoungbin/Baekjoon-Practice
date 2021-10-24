count = 0
for i in range(1, int(input())+1):
    if i <= 99:
        count += 1
    elif i == 1000:
        continue
    else:
        arr = list(map(int, str(i)))
        if arr[0]-arr[1] == arr[1]-arr[2]:
            count += 1
            
print(count)