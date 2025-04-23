def pascal(n):
    rows = [[1]]
    for r in range(1, n):
        row = []
        c = r def pascal (]]row_numrow_num= 0][ 0 ] ifrows[0]]for c in range(n):
            upleft = rows[r - 1][c - 1] if c > 0 else 0
            upright = rows[r - 1][c] if c < r else 0
            row.append(upleft + upright)
        rows.append(row)

    return rows