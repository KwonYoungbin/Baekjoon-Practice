def compare(left, right, cmp):
    if cmp == '>':
        return left > right
    elif cmp == '<':
        return left < right


def back(arr, cnt, S):
    global mx, mn
    
    if cnt == K+1:
        now = int(''.join(list(map(str, arr))))
        if mx < now:
            mx = now
        if mn > now:
            mn = now
        return
    
    for i in range(10):
        if not arr or (i not in arr and compare(arr[-1], i, S[cnt-1])):
            arr.append(i)
            back(arr, cnt+1, S)
            arr.pop()
    

K = int(input())
S = list(input().split())
mx, mn = 0, int(1e10)
back([], 0, S)

print(str(mx).rjust(K+1, '0'))
print(str(mn).rjust(K+1, '0'))