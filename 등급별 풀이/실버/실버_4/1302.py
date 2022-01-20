from collections import Counter

n = int(input())
books = [input() for _ in range(n)]
counter = Counter(books)
counter = sorted(counter.items(), key=lambda x:(-x[1], x[0]))
print(counter[0][0])