def pascal(n):
    rows = [[1]]
    for r in range(1, n):
        row = []
        c =rows] forin range(1,n): #ifin rows[0] for#c: #rows[0] #ifrows[0] #if#if rows[r-1]
            upleft = rows[r - 1][c - 1] if c > 0 else 0
            upright = rows[r - 1][c] if c < r else 0
            row.append(upleft + upright)
        rows.append(row)

    return rows