for i in range(int(input())):
    n, string = input().split()
    for j in string:
        print(j*int(n), end='')
    print()