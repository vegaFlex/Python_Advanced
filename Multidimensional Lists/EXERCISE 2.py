def is_inside(size, r, c):
    if r in range(size) and c in range(size):
        return True
    return False


presents_count = int(input())
size = int(input())
mtrx = [[x for x in input().split()] for _ in range(size)]

curr_presents_count = presents_count

santa_row, santa_col = 0, 0
nice_kids = 0

for row in range(size):
    for col in range(size):
        if mtrx[row][col] == 'S':
            santa_row, santa_col = row, col
        elif mtrx[row][col] == 'V':
            nice_kids += 1

curr_nice_kids = nice_kids

directions = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1)
}

while True:
    line = input()
    if line == 'Christmas morning' or curr_presents_count == 0:
        break

    next_row, next_col = directions[line](santa_row, santa_col)

    if is_inside(size, next_row, next_col):
        # if mtrx[next_row][next_col] == '-':
        #     mtrx[santa_row][santa_col] = '-'
        #     santa_row, santa_col = next_row, next_col
        #     mtrx[santa_row][santa_col] = 'S'
        #     continue

        if mtrx[next_row][next_col] == 'V':
            curr_presents_count -= 1
            mtrx[santa_row][santa_col] = '-'

            santa_row, santa_col = next_row, next_col
            mtrx[santa_row][santa_col] = 'S'
            curr_nice_kids -= 1

        elif mtrx[next_row][next_col] == 'C':
            mtrx[santa_row][santa_col] = '-'

            # old_santa_row, old_santa_col = santa_row, santa_col

            santa_row, santa_col = next_row, next_col
            mtrx[santa_row][santa_col] = 'S'

            for dir in directions:
                next_row, next_col = directions[dir](santa_row, santa_col)
                if is_inside(size, next_row, next_col):
                    if mtrx[next_row][next_col] == 'V' or mtrx[next_row][next_col] == 'X' and curr_presents_count > 0:
                        if mtrx[next_row][next_col] == 'V':
                            curr_nice_kids -= 1
                        curr_presents_count -= 1
                        mtrx[next_row][next_col] = '-'
            break

        else:
            mtrx[santa_row][santa_col] = '-'
            santa_row, santa_col = next_row, next_col
            mtrx[santa_row][santa_col] = 'S'

if curr_presents_count == 0:
    print(f"Santa ran out of presents!")

[print(*row) for row in mtrx]

if curr_nice_kids == 0:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {curr_nice_kids} nice kid/s.")
