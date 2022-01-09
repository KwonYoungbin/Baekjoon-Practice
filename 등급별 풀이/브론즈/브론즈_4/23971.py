import math
h, w, n, m = map(int, input().split())
print(math.ceil(w/(m+1)) * math.ceil(h/(n+1)))