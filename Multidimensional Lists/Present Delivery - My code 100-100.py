presents = int(input())
size = int(input())

mtrx = [[x for x in input().split()] for _ in range(size)]

santa_row, santa_col = 0, 0
nice_kids = 0

for row_i in range(size):
    for col_i in range(size):
        if mtrx[row_i][col_i] == 'S':
            santa_row, santa_col = row_i, col_i
        elif mtrx[row_i][col_i] == 'V':
            nice_kids += 1

directions = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1)
}
gaved_nice_kids = 0

while presents > 0:
    mtrx[santa_row][santa_col] = '-'
    command = input()

    if command == 'Christmas morning':
        break

    next_row, next_col = directions[command](santa_row, santa_col)

    if mtrx[next_row][next_col] == 'V':
        presents -= 1
        gaved_nice_kids += 1
        # mtrx[santa_row][santa_col] = '-'
        santa_row, santa_col = next_row, next_col


    elif mtrx[next_row][next_col] == 'C':
        santa_row, santa_col = next_row, next_col

        for dir in directions:
            next_row, next_col = directions[dir](santa_row, santa_col)
            if mtrx[next_row][next_col] == 'V':
                mtrx[next_row][next_col] = '-'
                presents -= 1
                gaved_nice_kids += 1

            elif mtrx[next_row][next_col] == 'X':
                mtrx[next_row][next_col] = '-'
                presents -= 1

    elif mtrx[next_row][next_col] == 'X':
        # mtrx[santa_row][santa_col] = '-'
        santa_row, santa_col = next_row, next_col
        # mtrx[santa_row][santa_col] = '-'


    elif mtrx[next_row][next_col] == '-':
        santa_row, santa_col = next_row, next_col

    # if command == 'Christmas morning' or presents == 0:
    #     break

mtrx[santa_row][santa_col] = 'S'

if presents == 0 and nice_kids - gaved_nice_kids != 0:
    print("Santa ran out of presents!")

[print(*row) for row in mtrx]

if nice_kids - gaved_nice_kids == 0:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids - gaved_nice_kids} nice kid/s.")
