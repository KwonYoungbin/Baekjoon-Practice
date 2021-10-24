string = input()

for i in range(ord('a'), ord('z')+1):
    print(string.find(chr(i)), end=' ')