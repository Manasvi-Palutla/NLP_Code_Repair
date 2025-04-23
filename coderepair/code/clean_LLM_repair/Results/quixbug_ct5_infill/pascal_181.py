def pascal(n):
    rows = [[1]]
    for r in range(1, n):
        row = []
        c = def pascal_rows (rows) :for c= rows[r][c-1] if]
            upleft = rows[r - 1][c - 1] if c > 0 else 0
            upright = rows[r - 1][c] if c < r else 0
            row.append(upleft + upright)
        rows.append(row)

    return rows