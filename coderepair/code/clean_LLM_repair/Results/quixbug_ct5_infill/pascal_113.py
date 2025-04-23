def pascal(n):
    rows = [[1]]
    for r in range(1, n):
        row = []
        for c in range(1,n):rows[0]] defr )= 0] if c > 0:= rows[c]1[0] if celse+ upright] if[ 1 ]else
            upleft = rows[r - 1][c - 1] if c > 0 else 0
            upright = rows[r - 1][c] if c < r else 0
            row.append(upleft + upright)
        rows.append(row)

    return rows