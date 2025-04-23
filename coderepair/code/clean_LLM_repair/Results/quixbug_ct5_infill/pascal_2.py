def pascal(n):
    rows = [[1]]
    for r in range(1, n):
        row = []
        c =[ ][ 0 ]rowsc1, c2):=c1, c2):rows=[c,c2]c2=1, c]c0,rows =0] }
            upleft = rows[r - 1][c - 1] if c > 0 else 0
            upright = rows[r - 1][c] if c < r else 0
            row.append(upleft + upright)
        rows.append(row)

    return rows