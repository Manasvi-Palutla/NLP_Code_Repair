def pascal(n):
    rows = [[1]]
    for r in range(1, n):
        row = []
        c = 1.]]for c1] [ c- 1if c < 00]if c <:[1]r
            upleft = rows[r - 1][c - 1] if c > 0 else 0
            upright = rows[r - 1][c] if c < r else 0
            row.append(upleft + upright)
        rows.append(row)

    return rows