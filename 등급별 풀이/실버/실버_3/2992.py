arr = list(map(int, input()))
chk_list = [0]*len(arr)

i = j = len(arr)-1

while i > 0 and arr[i-1] >= arr[i]:
    i -= 1

if i == 0:
    print(0)
else:
    while arr[i-1] >= arr[j]:
        j -= 1
    
    arr[i-1], arr[j] = arr[j], arr[i-1]
    print(''.join(map(str,(arr[:i] + sorted(arr[i:])))))