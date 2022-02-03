S = input()
arr = set()

for i in range(len(S)):
    for j in range(i+1, len(S)+1):
        arr.add(S[i:j])
print(len(arr))