for i in range(int(input())):
    N = int(input())
    dic = {'B': 0, 'W': 0}
    origin = input()
    destination = input()
    
    for x, y in zip(origin, destination):
        if x != y:
            dic[x] += 1
    
    total = dic['B'] + dic['W']
    min_cnt = min(dic['B'], dic['W'])
    print(total - min_cnt)