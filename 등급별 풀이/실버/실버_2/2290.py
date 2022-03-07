S, N = map(int, input().split())
arr = list(str(N))

for i in range(2*S+3):
    for val in arr:
        if i == 0:
            if val == '1' or val == '4':
                print(' '*(S+2), end='')
            else:
                print(' '+'-'*S+' ', end='')
        elif i == (2*S+3)//2:
            if val == '1' or val == '7' or val == '0':
                print(' '*(S+2), end='')
            else:
                print(' '+'-'*S+' ', end='')
        elif i == 2*S+2:
            if val == '1' or val == '4' or val == '7':
                print(' '*(S+2), end='')
            else:
                print(' '+'-'*S+' ', end='')
        elif i < (2*S+3)//2:
            if val == '1' or val == '2' or val == '3' or val == '7':
                print(' '*(S+1)+'|', end='')
            elif val == '5' or val == '6':
                print('|'+' '*(S+1), end='')
            else:
                print('|'+' '*S+'|', end='')
        else:
            if val == '6' or val == '8' or val == '0':
                print('|'+' '*S+'|', end='')
            elif val == '2':
                print('|'+' '*(S+1), end='')
            else:
                print(' '*(S+1)+'|', end='')
        print(' ', end='')
    print()