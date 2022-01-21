cards = [list(input().split()) for _ in range(5)]
cards.sort(key=lambda x: int(x[1]))
for i in range(5):
    cards[i][1] = int(cards[i][1])
    
score = 0

if cards[0][0] == cards[1][0] == cards[2][0] == cards[3][0] == cards[4][0] and cards[4][1]-cards[3][1] == cards[3][1]-cards[2][1] == cards[2][1]-cards[1][1] == cards[1][1]-cards[0][1] == 1:
    score = 900 + cards[4][1]
elif cards[0][1] == cards[1][1] == cards[2][1] == cards[3][1] or cards[1][1] == cards[2][1] ==cards[3][1] == cards[4][1]:
    score = 800 + cards[1][1]
elif (cards[0][1] == cards[1][1] == cards[2][1] and cards[3][1] == cards[4][1]) or (cards[4][1] == cards[3][1] == cards[2][1] and cards[0][1] == cards[1][1]):
    if cards[1][1] == cards[2][1]:
        score = cards[2][1]*10 + cards[3][1] + 700
    else:
        score = cards[2][1]*10 + cards[1][1] + 700
elif cards[0][0] == cards[1][0] == cards[2][0] == cards[3][0] == cards[4][0]:
    score = cards[4][1] + 600
elif cards[4][1]-cards[3][1] == cards[3][1]-cards[2][1] == cards[2][1]-cards[1][1] == cards[1][1]-cards[0][1] == 1:
    score = cards[4][1] + 500
elif (cards[0][1] == cards[1][1] == cards[2][1]) or (cards[1][1] == cards[2][1] == cards[3][1]) or (cards[2][1] == cards[3][1] == cards[4][1]):
    score = cards[2][1] + 400
elif (cards[0][1] == cards[1][1] and cards[2][1] == cards[3][1]) or (cards[0][1] == cards[1][1] and cards[3][1] == cards[4][1]) or (cards[1][1] == cards[2][1] and cards[3][1] == cards[4][1]):
    score = cards[3][1]*10 + cards[1][1] + 300
elif cards[0][1] == cards[1][1] or cards[1][1] == cards[2][1]:
    score = cards[1][1] + 200
elif cards[2][1] == cards[3][1] or cards[3][1] == cards[4][1]:
    score = cards[3][1] + 200
else:
    score = cards[4][1] + 100
print(score)