k = int(input())
arr = [list(map(int, input().split())) for _ in range(6)]

max_width, max_height = 0, 0
max_width_idx, max_height_idx = 0, 0

for i in range(6):
    if 1 <= arr[i][0] <= 2:
        if arr[i][1] > max_width:
            max_width = arr[i][1]
            max_width_idx = i
    else:
        if arr[i][1] > max_height:
            max_height = arr[i][1]
            max_height_idx = i
            
min_width = abs(arr[(max_width_idx-1) % 6][1] - arr[(max_width_idx+1) % 6][1])
min_height = abs(arr[(max_height_idx-1) % 6][1] - arr[(max_height_idx+1) % 6][1])
print(((max_width*max_height) - (min_width*min_height)) * k)