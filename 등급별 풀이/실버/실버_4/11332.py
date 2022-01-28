import math

per_sec = int(1e8)
for _ in range(int(input())):
    line = input().split()
    N, T, L = map(int, line[1:])
    if line[0] == 'O(N)':
        print('May Pass.' if N*T <= L*per_sec else 'TLE!')
    elif line[0] == 'O(N^2)':
        print('May Pass.' if (N**2)*T <= L*per_sec else 'TLE!')
    elif line[0] == 'O(N^3)':
        print('May Pass.' if (N**3)*T <= L*per_sec else 'TLE!')
    elif line[0] == 'O(2^N)':
        print('May Pass.' if (2**N)*T <= L*per_sec else 'TLE!')
    elif line[0] == 'O(N!)':
        print('May Pass.' if math.factorial(N)*T <= L*per_sec else 'TLE!')