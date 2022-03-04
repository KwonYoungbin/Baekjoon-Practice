def hanoi(n, from_pos, to_pos, support):
    if n == 1:
        print(from_pos, to_pos)
        return
    
    hanoi(n-1, from_pos, support, to_pos)
    print(from_pos, to_pos)
    hanoi(n-1, support, to_pos, from_pos)

N = int(input())
print((1 << N) - 1)

if N <= 20:
    hanoi(N, 1, 3, 2)