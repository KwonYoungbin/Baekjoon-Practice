arr = []
for i in range(1,10):
    arr.append([i,int(input())])
    
arr = sorted(arr, key=lambda x:x[1], reverse=True)
print(arr[0][1])
print(arr[0][0])