X = int(input())
sticks = [64]

while sum(sticks) != X:
    now = sticks.pop()
    divide = now//2
    if divide > 0:
        sticks.append(divide)
    if sum(sticks) < X:
        sticks.append(divide)
print(len(sticks))