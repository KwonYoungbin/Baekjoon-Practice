S = int(input())
arr = [0]
adder = 1
while arr[-1] < S:
    arr.append(arr[-1] + adder)
    adder += 1

if arr[-1] == S:
    print(len(arr)-1)
else:
    print(len(arr)-2)