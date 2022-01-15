n = input()
words = []

for f in range(len(n)-2):
    for s in range(f+1, len(n)-1):
        left = n[ : f+1][::-1]
        center = n[f+1 : s+1][::-1]
        right = n[s+1 : ][::-1]
        words.append(left + center + right)
words.sort()
print(words[0])