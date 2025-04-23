def pascal(n):
    rows = [[1]]
    for r in range(1, n):
        row = []
        c = r[ 0:]:c- 1 ]> 0 else)
WWW row#if rows[r][c]=[c]c-1] if c >elselen(rows):(rows[r][c])row.append(upleft+upright)
            upleft = rows[r - 1][c - 1] if c > 0 else 0
            upright = rows[r - 1][c] if c < r else 0
            row.append(upleft + upright)
        rows.append(row)

    return rows