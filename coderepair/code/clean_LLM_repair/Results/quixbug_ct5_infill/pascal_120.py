def pascal(n):
    rows = [[1]]
    for r in range(1, n):
        row = []
        c = r[(rows)  def1:1] =rows[0][r] if celse 0

CTYPE if1][c] if c0 else] if: if upleft > 0:row.append(upleft)else :
            upleft = rows[r - 1][c - 1] if c > 0 else 0
            upright = rows[r - 1][c] if c < r else 0
            row.append(upleft + upright)
        rows.append(row)

    return rows