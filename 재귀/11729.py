num = int(input())
def hanoi(n, _from, _to, _serv):
    if n == 1:
        print('%d %d'%(_from,_to))
        return
    
    hanoi(n-1, _from, _serv, _to)
    print('%d %d'%(_from,_to))
    hanoi(n-1, _serv, _to, _from)
    
print(2**num - 1)
hanoi(num, 1, 3, 2)