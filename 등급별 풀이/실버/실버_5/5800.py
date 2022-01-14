k = int(input())

for i in range(1, k+1):
    arr = list(map(int, input().split()))
    scores = arr[1:]
    scores.sort(reverse=True)
    
    max_gap = 0
    for j in range(arr[0]-1):
        max_gap = max(scores[j] - scores[j+1], max_gap)
    
    print("Class %d" %(i))
    print("Max %d, Min %d, Largest gap %d" %(scores[0], scores[-1], max_gap))