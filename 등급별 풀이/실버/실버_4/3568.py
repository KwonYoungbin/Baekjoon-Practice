arr = input().replace(',','').replace(';','').split()

for i in range(1, len(arr)):
    print(arr[0], end='')
    for j in range(len(arr[i])-1, 0, -1):
        if not arr[i][j].isalpha():
            if arr[i][j] == ']':
                print('[', end='')
            elif arr[i][j] == '[':
                print(']', end='')
            else:
                print(arr[i][j], end='')
    print(' ', end='')
    for j in range(len(arr[i])):
        if arr[i][j].isalpha():
            print(arr[i][j], end='')
    print(';')