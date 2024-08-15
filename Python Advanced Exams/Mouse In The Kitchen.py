def is_valid(rowwss, collss, roww, coll):
    if roww not in range(rowwss) or coll not in range(collss):
        return False
    return True


rows, cols = [int(x) for x in input().split(',')]
mtrx = [list(input()) for _ in range(rows)]

all_cheeses = 0
mouse_row, mouse_col = 0, 0
for row_i in range(rows):
    for col_i in range(cols):
        if mtrx[row_i][col_i] == 'M':
            mouse_row, mouse_col = row_i, col_i
        elif mtrx[row_i][col_i] == 'C':
            all_cheeses += 1

directions = {
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c)
}
while True:
    command = input()
    if command == 'danger':
        print("Mouse will come back later!")
        break

    next_row, next_col = directions[command](mouse_row, mouse_col)

    if not is_valid(rows, cols, next_row, next_col):
        print("No more cheese for tonight!")
        break

    if mtrx[next_row][next_col] == '*':
        mtrx[mouse_row][mouse_col] = '*'
        mouse_row, mouse_col = next_row, next_col
        mtrx[mouse_row][mouse_col] = 'M'
        continue

    if mtrx[next_row][next_col] == 'C':
        all_cheeses -= 1
        mtrx[mouse_row][mouse_col] = '*'
        mouse_row, mouse_col = next_row, next_col
        mtrx[mouse_row][mouse_col] = 'M'

        if all_cheeses == 0:
            print("Happy mouse! All the cheese is eaten, good night!")
            break

    if mtrx[next_row][next_col] == 'T':
        mtrx[mouse_row][mouse_col] = "*"
        mouse_row, mouse_col = next_row, next_col
        mtrx[mouse_row][mouse_col] = "M"
        print("Mouse is trapped!")
        break

    if mtrx[next_row][next_col] == '@':
        continue

[print(''.join(row)) for row in mtrx]
