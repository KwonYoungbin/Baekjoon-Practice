king, stone, N = input().split()

rows = ['1','2','3','4','5','6','7','8']
cols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
moves = [(0,1), (0,-1), (-1,0), (1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
directions = ['R', 'L', 'B', 'T', 'RT', 'LT', 'RB', 'LB']
king_row_idx = rows.index(king[1])
king_col_idx = cols.index(king[0])
stone_row_idx = rows.index(stone[1])
stone_col_idx = cols.index(stone[0])

for _ in range(int(N)):
    idx = directions.index(input())
    
    new_row = king_row_idx + moves[idx][0]
    new_col = king_col_idx + moves[idx][1]
    new_stone_row = stone_row_idx
    new_stone_col = stone_col_idx
    if new_col < 0 or new_col >= 8 or new_row < 0 or new_row >= 8:
        continue
    elif new_row == stone_row_idx and new_col == stone_col_idx:
        new_stone_row = stone_row_idx + moves[idx][0]
        new_stone_col = stone_col_idx + moves[idx][1]
        if new_stone_col < 0 or new_stone_col >= 8 or new_stone_row < 0 or new_stone_row >= 8:
            continue
    king_col_idx = new_col
    king_row_idx = new_row
    stone_col_idx = new_stone_col
    stone_row_idx = new_stone_row

print(cols[king_col_idx]+rows[king_row_idx])
print(cols[stone_col_idx]+rows[stone_row_idx])