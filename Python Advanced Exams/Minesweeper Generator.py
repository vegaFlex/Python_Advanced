import re


def possible_asterisk(r, c, matrix):
    directions = [(r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1)]

    count_asterisk_around = 0
    for roww, coll in directions:
        if roww in range(len(matrix)) and coll in range(len(matrix)) and mtrx[roww][coll] == '*':
            count_asterisk_around += 1

    return count_asterisk_around


n = int(input())
bombs_count = int(input())
mtrx = [[''] * n for _ in range(n)]

for _ in range(bombs_count):
    row_i, col_i = [int(x) for x in re.findall('\\d+', input())]
    mtrx[row_i][col_i] = '*'

for row in range(n):
    for col in range(n):
        if mtrx[row][col] != '*':
            mtrx[row][col] = possible_asterisk(row, col, mtrx)

[print(*row)for row in mtrx]
