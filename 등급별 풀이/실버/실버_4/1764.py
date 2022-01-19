import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nolisten = set([input().strip() for _ in range(n)])
nolook = set([input().strip() for _ in range(m)])
nolisten_n_nolook = nolisten & nolook

print(len(nolisten_n_nolook))
print(*sorted(nolisten_n_nolook), sep='\n')