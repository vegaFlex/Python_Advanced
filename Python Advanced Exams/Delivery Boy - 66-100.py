rows, cols = [int(x) for x in input().split()]
mtrx = [list(input()) for _ in range(rows)]


def is_valid(r, c, rowws, colls):
    if r in range(rowws) and c in range(colls):
        return True
    return False


directions = {
    'up': lambda row, col: (row - 1, col),
    'down': lambda row, col: (row + 1, col),
    'left': lambda row, col: (row, col - 1),
    'right': lambda row, col: (row, col + 1)
}

initial_row, initial_col = 0, 0
player_row, player_col = 0, 0

for row in range(rows - 1):
    for col in range(cols - 1):

        a = mtrx[row][col]
        if mtrx[row][col] == 'B':
            player_row, player_col = row, col
            initial_row, initial_col = row, col

while True:
    command = input()
    next_row, next_col = directions[command](player_row, player_col)

    # if next_row not in range(rows) or next_col not in range(cols):
    if not is_valid(next_row, next_col, rows, cols):

        mtrx[initial_row][initial_col] = ' '
        print("The delivery is late. Order is canceled.")
        break

    # if mtrx[next_row][next_col] == '*':
    #     continue
    else:
        if mtrx[next_row][next_col] == '-':
            player_row, player_col = next_row, next_col
            mtrx[player_row][player_col] = '.'

        elif mtrx[next_row][next_col] == 'P':
            player_row, player_col = next_row, next_col
            mtrx[player_row][player_col] = '.'
            mtrx[player_row][player_col] = 'R'
            print("Pizza is collected. 10 minutes for delivery.")
            continue

        elif mtrx[next_row][next_col] == 'A':
            player_row, player_col = next_row, next_col
            mtrx[player_row][player_col] = '.'
            mtrx[player_row][player_col] = 'P'
            print("Pizza is delivered on time! Next order...")
            break

[print(''.join(row)) for row in mtrx]
