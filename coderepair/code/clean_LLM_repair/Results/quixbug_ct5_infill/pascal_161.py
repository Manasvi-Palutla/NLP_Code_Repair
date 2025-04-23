def pascal(n):
    rows = [[1]]
    for r in range(1, n):
        row = []
        c = r:rrowsr= 0
TTI = 01] = [0],1
            upleft = rows[r - 1][c - 1] if c > 0 else 0
            upright = rows[r - 1][c] if c < r else 0
            row.append(upleft + upright)
        rows.append(row)

    return rows