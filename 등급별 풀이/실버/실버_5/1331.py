from collections import Counter

col = ['A','B','C','D','E','F']
row = ['1','2','3','4','5','6']
pos = [input() for _ in range(36)]
counter = Counter(pos)

if len(counter.values()) != 36:
    print('Invalid')
else:
    valid = True
    pos.append(pos[0])
    for i in range(1, len(pos)):
        col_idx = col.index(pos[i-1][0])
        row_idx = row.index(pos[i-1][1])
        possible = []
        
        if 0 <= col_idx-2 <= 5:
            if 0 <= row_idx-1 <= 5:
                possible.append(col[col_idx-2]+row[row_idx-1])
            if 0 <= row_idx+1 <= 5:
                possible.append(col[col_idx-2]+row[row_idx+1])
        
        if 0 <= col_idx+2 <= 5:
            if 0 <= row_idx-1 <= 5:
                possible.append(col[col_idx+2]+row[row_idx-1])
            if 0 <= row_idx+1 <= 5:
                possible.append(col[col_idx+2]+row[row_idx+1])
                
        if 0 <= row_idx-2 <= 5:
            if 0 <= col_idx-1 <= 5:
                possible.append(col[col_idx-1]+row[row_idx-2])
            if 0 <= col_idx+1 <= 5:
                possible.append(col[col_idx+1]+row[row_idx-2])
                
        if 0 <= row_idx+2 <= 5:
            if 0 <= col_idx-1 <= 5:
                possible.append(col[col_idx-1]+row[row_idx+2])
            if 0 <= col_idx+1 <= 5:
                possible.append(col[col_idx+1]+row[row_idx+2])
        
        if pos[i] not in possible:
            valid = False
            break

    print('Valid' if valid else 'Invalid')